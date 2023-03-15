import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html
from random import random

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=boxplot-multi

minVal = 0
maxVal = 200

def makeData():
    data = []
    for ii in range(0, 15):
        cate = []
        for jj in range(0, 100):
            cate.append(random() * maxVal)
        data.append(cate)
    return data

def main():
    app = Dash(__name__)

    data0 = makeData()
    data1 = makeData()
    data2 = makeData()

    option = {
        'title': {
            'text': 'Multiple Categories',
            'left': 'center'
        },
        'dataset': [
            {
                'source': data0
            },
            {
                'source': data1
            },
            {
                'source': data2
            },
            {
                'fromDatasetIndex': 0,
                'transform': {'type': 'boxplot'}
            },
            {
                'fromDatasetIndex': 1,
                'transform': {'type': 'boxplot'}
            },
            {
                'fromDatasetIndex': 2,
                'transform': {'type': 'boxplot'}
            }
        ],
        'legend': {
            'top': '10%'
        },
        'tooltip': {
            'trigger': 'item',
            'axisPointer': {
                'type': 'shadow'
            }
        },
        'grid': {
            'left': '10%',
            'top': '20%',
            'right': '10%',
            'bottom': '15%'
        },
        'xAxis': {
            'type': 'category',
            'boundaryGap': True,
            'nameGap': 30,
            'splitArea': {
                'show': True
            },
            'splitLine': {
                'show': False
            }
        },
        'yAxis': {
            'type': 'value',
            'name': 'Value',
            'min': minVal,
            'max': maxVal,
            'splitArea': {
                'show': False
            }
        },
        'dataZoom': [
            {
                'type': 'inside',
                'start': 0,
                'end': 20
            },
            {
                'show': True,
                'type': 'slider',
                'top': '90%',
                'xAxisIndex': [0],
                'start': 0,
                'end': 20
            }
        ],
        'series': [
            {
                'name': 'category0',
                'type': 'boxplot',
                'datasetIndex': 3
            },
            {
                'name': 'category1',
                'type': 'boxplot',
                'datasetIndex': 4
            },
            {
                'name': 'category2',
                'type': 'boxplot',
                'datasetIndex': 5
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
