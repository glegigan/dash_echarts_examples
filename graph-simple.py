import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=graph-simple


def main():
    app = Dash(__name__)

    option = {
        'title': {
            'text': 'Basic Graph'
        },
        'tooltip': {},
        'animationDurationUpdate': 1500,
        'animationEasingUpdate': 'quinticInOut',
        'series': [
            {
                'type': 'graph',
                'layout': 'none',
                'symbolSize': 50,
                'roam': True,
                'label': {
                    'show': True
                },
                'edgeSymbol': ['circle', 'arrow'],
                'edgeSymbolSize': [4, 10],
                'edgeLabel': {
                    'fontSize': 20
                },
                'data': [
                    {
                        'name': 'Node 1',
                        'x': 300,
                        'y': 300
                    },
                    {
                        'name': 'Node 2',
                        'x': 800,
                        'y': 300
                    },
                    {
                        'name': 'Node 3',
                        'x': 550,
                        'y': 100
                    },
                    {
                        'name': 'Node 4',
                        'x': 550,
                        'y': 500
                    }
                ],
                'links': [
                    {
                        'source': 0,
                        'target': 1,
                        'symbolSize': [5, 20],
                        'label': {
                            'show': True
                        },
                        'lineStyle': {
                            'width': 5,
                            'curveness': 0.2
                        }
                    },
                    {
                        'source': 'Node 2',
                        'target': 'Node 1',
                        'label': {
                            'show': True
                        },
                        'lineStyle': {
                            'curveness': 0.2
                        }
                    },
                    {
                        'source': 'Node 1',
                        'target': 'Node 3'
                    },
                    {
                        'source': 'Node 2',
                        'target': 'Node 3'
                    },
                    {
                        'source': 'Node 2',
                        'target': 'Node 4'
                    },
                    {
                        'source': 'Node 1',
                        'target': 'Node 4'
                    }
                ],
                'lineStyle': {
                    'opacity': 0.9,
                    'width': 2,
                    'curveness': 0
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
