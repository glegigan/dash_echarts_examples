from random import random
import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=graph-grid


def main():
    app = Dash(__name__)

    axisData = ['Mon', 'Tue', 'Wed', 'Very Loooong Thu', 'Fri', 'Sat', 'Sun']
    data = [round(random() * 1000 * (ii + 1)) for ii, item in enumerate(axisData)]
    links = [{'source': ii, 'target': ii + 1} for ii, item in enumerate(axisData)]

    option = {
        'title': {
            'text': 'Graph on Cartesian'
        },
        'tooltip': {},
        'xAxis': {
            'type': 'category',
            'boundaryGap': False,
            'data': axisData
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [
            {
                'type': 'graph',
                'layout': 'none',
                'coordinateSystem': 'cartesian2d',
                'symbolSize': 40,
                'label': {
                    'show': True
                },
                'edgeSymbol': ['circle', 'arrow'],
                'edgeSymbolSize': [4, 10],
                'data': data,
                'links': links,
                'lineStyle': {
                    'color': '#2f4554'
                }
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
