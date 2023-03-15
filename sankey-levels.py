import json
import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=sankey-levels


def main():
    app = Dash(__name__)

    with open('./static/product.json') as f:
        data = json.load(f)

    option = {
        'title': {
            'text': 'Sankey Diagram'
        },
        'tooltip': {
            'trigger': 'item',
            'triggerOn': 'mousemove'
        },
        'series': [
            {
                'type': 'sankey',
                'data': data['nodes'],
                'links': data['links'],
                'emphasis': {
                    'focus': 'adjacency'
                },
                'levels': [
                    {
                        'depth': 0,
                        'itemStyle': {
                            'color': '#fbb4ae'
                        },
                        'lineStyle': {
                            'color': 'source',
                            'opacity': 0.6
                        }
                    },
                    {
                        'depth': 1,
                        'itemStyle': {
                            'color': '#b3cde3'
                        },
                        'lineStyle': {
                            'color': 'source',
                            'opacity': 0.6
                        }
                    },
                    {
                        'depth': 2,
                        'itemStyle': {
                            'color': '#ccebc5'
                        },
                        'lineStyle': {
                            'color': 'source',
                            'opacity': 0.6
                        }
                    },
                    {
                        'depth': 3,
                        'itemStyle': {
                            'color': '#decbe4'
                        },
                        'lineStyle': {
                            'color': 'source',
                            'opacity': 0.6
                        }
                    }
                ],
                'lineStyle': {
                    'curveness': 0.5
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
