import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html


# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=mix-line-bar


def main():
    app = Dash(__name__)

    option = {
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': {
                'type': 'cross',
                'crossStyle': {
                    'color': '#999'
                }
            }
        },
        'toolbox': {
            'feature': {
                'dataView': {'show': True, 'readOnly': False},
                'magicType': {'show': True, 'type': ['line', 'bar']},
                'restore': {'show': True},
                'saveAsImage': {'show': True}
            }
        },
        'legend': {
            'data': ['Evaporation', 'Precipitation', 'Temperature']
        },
        'xAxis': [
            {
                'type': 'category',
                'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                'axisPointer': {
                    'type': 'shadow'
                }
            }
        ],
        'yAxis': [
            {
                'type': 'value',
                'name': 'Precipitation',
                'min': 0,
                'max': 250,
                'interval': 50,
                'axisLabel': {
                    'formatter': '{value} ml'
                }
            },
            {
                'type': 'value',
                'name': 'Temperature',
                'min': 0,
                'max': 25,
                'interval': 5,
                'axisLabel': {
                    'formatter': '{value} °C'
                }
            }
        ],
        'series': [
            {
                'name': 'Evaporation',
                'type': 'bar',
                'tooltip': {
                    'valueFormatter': 'valueFormatterML'
                },
                'data': [
                    2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3
                ]
            },
            {
                'name': 'Precipitation',
                'type': 'bar',
                'tooltip': {
                    'valueFormatter': 'valueFormatterML'
                },
                'data': [
                    2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3
                ]
            },
            {
                'name': 'Temperature',
                'type': 'line',
                'yAxisIndex': 1,
                'tooltip': {
                    'valueFormatter': 'valueFormatterC',
                },
                'data': [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
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
                        fun_keys=['valueFormatter', 'valueFormatter'],
                        funs={
                            'valueFormatterML': '''
                            function(value) {
                            return value + ' ml';
                            }
                            ''',
                            'valueFormatterC': '''
                            function(value) {
                            return value + ' °C';
                            }
                            ''',
                        },
                        style={
                            'width': '98vw',
                            'height': '98vh',
                        }
                    ),
                ]
            ),
        ],
    )

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
