import dash_echarts
from dash import Dash, dcc, html
from random import random
from datetime import datetime, timedelta

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=pictorialBar-dotted


def main():
    app = Dash(__name__)

    category = []
    lineData = []
    barData = []
    now = datetime.now()
    for ii in range(0, 20):
        category.append((now + timedelta(days=ii)).strftime("%Y-%m-%d"))
        b = random() * 200
        d = random() * 200
        barData.append(b)
        lineData.append(d + b)

    option = {
        'backgroundColor': '#0f375f',
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': {
                'type': 'shadow'
            }
        },
        'legend': {
            'data': ['line', 'bar'],
            'textStyle': {
                'color': '#ccc'
            }
        },
        'xAxis': {
            'data': category,
            'axisLine': {
                'lineStyle': {
                    'color': '#ccc'
                }
            }
        },
        'yAxis': {
            'splitLine': {'show': False},
            'axisLine': {
                'lineStyle': {
                    'color': '#ccc'
                }
            }
        },
        'series': [
            {
                'name': 'line',
                'type': 'line',
                'smooth': True,
                'showAllSymbol': True,
                'symbol': 'emptyCircle',
                'symbolSize': 15,
                'data': lineData
            },
            {
                'name': 'bar',
                'type': 'bar',
                'barWidth': 10,
                'itemStyle': {
                    'borderRadius': 5,
                    'color': {
                        'colorStops': [
                            {'offset': 0, 'color': '#14c8d4'},
                            {'offset': 1, 'color': '#43eec6'},
                        ],
                        'x': 0,
                        'y': 0,
                        'x2': 0,
                        'y2': 1,
                        'type': 'linear',
                        'global': False,
                    }
                },
                'data': barData
            },
            {
                'name': 'line',
                'type': 'bar',
                'barGap': '-100%',
                'barWidth': 10,
                'itemStyle': {
                    'color': {
                        'colorStops': [
                            {'offset': 0, 'color': 'rgba(20,200,212,0.5)'},
                            {'offset': 0.2, 'color': 'rgba(20,200,212,0.2)'},
                            {'offset': 1, 'color': 'rgba(20,200,212,0)'},
                        ],
                        'x': 0,
                        'y': 0,
                        'x2': 0,
                        'y2': 1,
                        'type': 'linear',
                        'global': False,
                    }
                },
                'z': -12,
                'data': lineData
            },
            {
                'name': 'dotted',
                'type': 'pictorialBar',
                'symbol': 'rect',
                'itemStyle': {
                    'color': '#0f375f'
                },
                'symbolRepeat': True,
                'symbolSize': [12, 4],
                'symbolMargin': 1,
                'z': -10,
                'data': lineData
            }
        ]
    }

    app.layout = html.Div(
        [
            dash_echarts.DashECharts(
                option=option,
                id='echarts',
                style={
                    "width": '98vw',
                    "height": '98vh',
                }
            ),
            dcc.Interval(id="interval", interval=2500, n_intervals=0),
        ]
    )

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
