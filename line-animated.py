import random

import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/


def gen_randlist(num):
    return random.sample(range(num), 7)


def main():
    app = Dash(__name__)

    option = {
        'line-smooth': {
            'xAxis': {
                'type': 'category',
                'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            },
            'yAxis': {
                'type': 'value'
            },
            'series': [
                {
                    'data': gen_randlist(200),
                    'type': 'line',
                    'smooth': True
                },
                {
                    'data': gen_randlist(200),
                    'type': 'line',
                    'smooth': True
                }
            ]
        }
    }

    '''
        Layout
    '''
    app.layout = html.Div(
        children=[
            dbc.Row(
                className='g-0',
                align='center',
                children=[
                    dash_echarts.DashECharts(
                        option=option,
                        id='echarts',
                        style={
                            "width": '98vw',
                            "height": '98vh',
                        }
                    ),
                ]
            ),
            dcc.Interval(id='interval', interval=1 * 1000, n_intervals=0),
        ],
    )

    @app.callback(
        output=Output(component_id='echarts', component_property='option'),
        inputs=[
            Input(component_id='interval', component_property= 'n_intervals')
        ]
    )
    def update_echarts(n_intervals):
        if n_intervals == 0:
            raise PreventUpdate
        else:
            option['line-smooth']['series'][0]['data'] = gen_randlist(200)
            option['line-smooth']['series'][1]['data'] = gen_randlist(200)
        return option['line-smooth']

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
