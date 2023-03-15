from random import random
import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html
import math

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=scatter-large


def genData(len: int, offset: int) -> list:
    arr = [0] * int(len * 2)
    off = 0
    for ii in range(int(len)):
        x = random() * 10
        y = math.sin(x) - x * (0.1 if len % 2 else -0.1) * random() + (offset or 0) / 10
        arr[off] = x
        off += 1
        arr[off] = y
        off += 1

    return arr


def main():
    app = Dash(__name__)

    data1 = genData(5e5, 0)
    data2 = genData(5e5, 10)

    option = {
        'title': {
            'text':
                str(len(data1) / 2 + len(data2) / 2) + ' Points'
        },
        'tooltip': {},
        'toolbox': {
            'left': 'center',
            'feature': {
                'dataZoom': {}
            }
        },
        'legend': {
            'orient': 'vertical',
            'right': 10
        },
        'xAxis': [{}],
        'yAxis': [{}],
        'dataZoom': [
            {
                'type': 'inside'
            },
            {
                'type': 'slider'
            }
        ],
        'animation': False,
        'series': [
            {
                'name': 'A',
                'type': 'scatter',
                'data': data1,
                'dimensions': ['x', 'y'],
                'symbolSize': 3,
                'itemStyle': {
                    'opacity': 0.4
                },
                'large': True
            },
            {
                'name': 'B',
                'type': 'scatter',
                'data': data2,
                'dimensions': ['x', 'y'],
                'symbolSize': 3,
                'itemStyle': {
                    'opacity': 0.4
                },
                'large': True
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

    app.run_server(debug=True)


if __name__ == '__main__':
    main()
