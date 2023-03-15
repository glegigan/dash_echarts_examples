import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html
import json

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=graph-npm


def main():
    app = Dash(__name__)

    with open('./static/npmdepgraph.min10.json') as f:
        jsonData = json.load(f)

    data = []
    for node in jsonData['nodes']:
        data.append(
            {
                'x': node['x'],
                'y': node['y'],
                'id': node['id'],
                'name': node['label'],
                'symbolSize': node['size'],
                'itemStyle': {
                    'color': node['color']
                }
            }
        )

    edges = []
    for edge in jsonData['edges']:
        edges.append(
            {
                'source': edge['sourceID'],
                'target': edge['targetID'],
            }
        )

    option = {
        'title': {
            'text': 'NPM Dependencies'
        },
        'animationDurationUpdate': 1500,
        'animationEasingUpdate': 'quinticInOut',
        'series': [
            {
                'type': 'graph',
                'layout': 'none',
                # progressiveThreshold: 700,
                'data': data,
                'edges': edges,
                'emphasis': {
                    'focus': 'adjacency',
                    'label': {
                        'position': 'right',
                        'show': True
                    }
                },
                'roam': True,
                'lineStyle': {
                    'width': 0.5,
                    'curveness': 0.3,
                    'opacity': 0.7
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
