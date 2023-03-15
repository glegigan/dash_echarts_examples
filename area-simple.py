from random import random
from datetime import date, timedelta

import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=area-simple


def main():
    app = Dash(__name__)

    base = date(1968, 9, 3)
    dateList = []
    data = [random() * 300]
    for ii in range(1, 20000):
        now = base + timedelta(days=ii)
        dateList.append(
            '/'.join([str(now.year), str(now.month + 1), str(now.day)])
        )
        data.append(
            round(
                (random() - 0.5) * 20 + data[ii - 1]
            )
        )

    option = {
        'tooltip': {
            'trigger': 'axis',
            'position': 'posFunc',
        },
        'title': {
            'left': 'center',
            'text': 'Large Area Chart'
        },
        'toolbox': {
            'feature': {
                'dataZoom': {
                    'yAxisIndex': 'none'
                },
                'restore': {},
                'saveAsImage': {}
            }
        },
        'xAxis': {
            'type': 'category',
            'boundaryGap': False,
            'data': dateList
        },
        'yAxis': {
            'type': 'value',
            'boundaryGap': [0, '100%']
        },
        'dataZoom': [
            {
                'type': 'inside',
                'start': 0,
                'end': 10
            },
            {
                'start': 0,
                'end': 10
            }
        ],
        'series': [
            {
                'name': 'Fake Data',
                'type': 'line',
                'symbol': 'none',
                'sampling': 'lttb',
                'itemStyle': {
                    'color': 'rgb(255, 70, 131)'
                },

                'areaStyle': {
                    'color': {
                        'colorStops': [
                            {'offset': 0, 'color': 'rgb(255, 158, 68)'},
                            {'offset': 1, 'color': 'rgb(255, 70, 131)'},
                        ],
                        'x': 0,
                        'y': 0,
                        'x2': 0,
                        'y2': 1,
                        'type': 'linear',
                        'global': False,
                    },
                },
                'data': data
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
                        fun_keys=['position'],
                        funs={
                            'posFunc': '''
                            function (pt) {
                                return [pt[0], '10%'];
                            }
                            '''
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
