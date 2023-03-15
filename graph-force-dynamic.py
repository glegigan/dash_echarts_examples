from random import random

import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=graph-force-dynamic


data = [
    {
        'fixed': True,
        'x': 2048 / 2,
        'y': 1176 / 2,
        'symbolSize': 20,
        'id': 0,
    }
]
edges = []


def main():
    app = Dash(__name__)

    option = {
        'series': [
            {
                'type': 'graph',
                'layout': 'force',
                'animation': False,
                'data': data,
                'force': {
                    # 'initLayout': 'circular'
                    # gravity: 0
                    'repulsion': 100,
                    'edgeLength': 5
                },
                'edges': edges
            }
        ]
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
            dcc.Interval(id='interval', interval=200, n_intervals=0),
        ],
    )

    @app.callback(
        output=Output(component_id='echarts', component_property='option'),
        inputs=[
            Input(component_id='interval', component_property='n_intervals')
        ]
    )
    def update_echarts(n_intervals):
        if n_intervals < 0:
            raise PreventUpdate
        else:
            COLOR_ALL = [
                '#37A2DA',
                '#e06343',
                '#37a354',
                '#b55dba',
                '#b5bd48',
                '#8378EA',
                '#96BFFF'
            ]
            data.append(
                {
                    'symbolSize': 10,
                    'id': len(data),
                    'itemStyle': {
                        'color': COLOR_ALL[len(data) % 7],
                    }
                }
            )

            source = round((len(data) - 1) * random())
            target = round((len(data) - 1) * random())

            if source != target:
                edges.append(
                    {
                        'source': source,
                        'target': target
                    }
                )

            option['series'][0] = {
                'roam': True,
                'data': data,
                'edges': edges
            }

            return option

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
