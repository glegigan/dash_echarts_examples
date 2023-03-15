import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=sunburst-borderRadius


def main():
    app = Dash(__name__)

    option = {
        'series': {
            'type': 'sunburst',
            'data': [
                {
                    'name': 'Grandpa',
                    'children': [
                        {
                            'name': 'Uncle Leo',
                            'value': 15,
                            'children': [
                                {
                                    'name': 'Cousin Jack',
                                    'value': 2
                                },
                                {
                                    'name': 'Cousin Mary',
                                    'value': 5,
                                    'children': [
                                        {
                                            'name': 'Jackson',
                                            'value': 2
                                        }
                                    ]
                                },
                                {
                                    'name': 'Cousin Ben',
                                    'value': 4
                                }
                            ]
                        },
                        {
                            'name': 'Father',
                            'value': 10,
                            'children': [
                                {
                                    'name': 'Me',
                                    'value': 5
                                },
                                {
                                    'name': 'Brother Peter',
                                    'value': 1
                                }
                            ]
                        }
                    ]
                },
                {
                    'name': 'Nancy',
                    'children': [
                        {
                            'name': 'Uncle Nike',
                            'children': [
                                {
                                    'name': 'Cousin Betty',
                                    'value': 1
                                },
                                {
                                    'name': 'Cousin Jenny',
                                    'value': 2
                                }
                            ]
                        }
                    ]
                }
            ],
            'radius': [60, '90%'],
            'itemStyle': {
                'borderRadius': 7,
                'borderWidth': 2
            },
            'label': {
                'show': True
            }
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
        ],
    )

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
