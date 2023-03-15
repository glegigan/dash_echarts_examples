import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=gauge-simple


def main():
    app = Dash(__name__)

    option = {
        'tooltip': {
            'formatter': '{a} <br/>{b} : {c}%'
        },
        'series': [
            {
                'name': 'Pressure',
                'type': 'gauge',
                'progress': {
                    'show': True,
                    'itemStyle': {
                        'color': {
                            'type': 'linear',
                            'x': 0,
                            'y': 1,
                            'x2': 1,
                            'y2': 1,
                            'colorStops': [
                                {
                                    'offset': 0,
                                    'color': "blue"
                                }, {
                                    'offset': 0.25,
                                    'color': "purple"
                                }, {
                                    'offset': 0.5,
                                    'color': "green"
                                }, {
                                    'offset': 0.75,
                                    'color': "orange"
                                }, {
                                    'offset': 1,
                                    'color': "red"
                                }
                            ],
                            'global': False
                        }
                    }
                },
                'detail': {
                    'valueAnimation': True,
                    'formatter': '{value}'
                },
                'data': [
                    {
                        'value': 70,
                        'name': 'SCORE'
                    }
                ]
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
        ],
    )

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
