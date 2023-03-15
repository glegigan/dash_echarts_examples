import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=line-stack


def main():
    app = Dash(__name__)

    option = {
        'color': ['#80FFA5', '#00DDFF', '#37A2FF', '#FF0087', '#FFBF00'],
        'title': {
            'text': 'Gradient Stacked Area Chart'
        },
        'tooltip': {
            'show': True,
            'trigger': 'axis',
            'axisPointer': {
                'type': 'cross',
                'label': {
                    'backgroundColor': '#6a7985'
                }
            }
        },
        'legend': {
            'data': ['Line 1', 'Line 2', 'Line 3', 'Line 4', 'Line 5']
        },
        'toolbox': {
            'feature': {
                'saveAsImage': {}
            }
        },
        'grid': {
            'left': '3%',
            'right': '4%',
            'bottom': '3%',
            'containLabel': True
        },
        'xAxis': [
            {
                'type': 'category',
                'boundaryGap': False,
                'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            }
        ],
        'yAxis': [
            {
                'type': 'value'
            }
        ],
        'series': [
            {
                'name': 'Line 1',
                'type': 'line',
                'stack': 'Total',
                'smooth': True,
                'lineStyle': {
                    'width': 2
                },
                'showSymbol': False,
                'emphasis': {
                    'focus': 'series'
                },
                'data': [140, 232, 101, 264, 90, 340, 250]
            },
            {
                'name': 'Line 2',
                'type': 'line',
                'stack': 'Total',
                'smooth': True,
                'lineStyle': {
                    'width': 2
                },
                'showSymbol': False,
                'emphasis': {
                    'focus': 'series'
                },
                'data': [120, 282, 111, 234, 220, 340, 310]
            },
            {
                'name': 'Line 3',
                'type': 'line',
                'stack': 'Total',
                'smooth': True,
                'lineStyle': {
                    'width': 2
                },
                'showSymbol': False,
                'emphasis': {
                    'focus': 'series'
                },
                'data': [320, 132, 201, 334, 190, 130, 220]
            },
            {
                'name': 'Line 4',
                'type': 'line',
                'stack': 'Total',
                'smooth': True,
                'lineStyle': {
                    'width': 2
                },
                'showSymbol': False,
                'emphasis': {
                    'focus': 'series'
                },
                'data': [220, 402, 231, 134, 190, 230, 120]
            },
            {
                'name': 'Line 5',
                'type': 'line',
                'stack': 'Total',
                'smooth': True,
                'lineStyle': {
                    'width': 2
                },
                'showSymbol': False,
                'label': {
                    'show': True,
                    'position': 'top'
                },
                'emphasis': {
                    'focus': 'series'
                },
                'data': [220, 302, 181, 234, 210, 290, 150]
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
