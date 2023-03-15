import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html
from math import floor

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=graph-force2


def createNodes(count):
    nodes = []
    for ii in range(count):
        nodes.append(
            {
                'id': ii
            }
        )
    return nodes


def createEdges(count):
    edges = []
    if count == 2:
        return [[0, 1]]
    for ii in range(count):
        edges.append([ii, (ii + 1) % count])
    return edges


def main():
    app = Dash(__name__)

    data = []
    for ii in range(16):
        data.append(
            {
                'nodes': createNodes(ii + 2),
                'edges': createEdges(ii + 2)
            }
        )

    option = {
        'series': [
            {
                'type': 'graph',
                'layout': 'force',
                'animation': False,
                'data': item['nodes'],
                'left': str((idx % 4) * 25) + '%',
                'top': str(floor(idx / 4) * 25) + '%',
                'width': '25%',
                'height': '25%',
                'force': {
                    # 'initLayout': 'circular'
                    # 'gravity': 0
                    'repulsion': 60,
                    'edgeLength': 2
                },
                'edges': [{'source': e[0], 'target': e[1]} for e in data[idx]['edges']],
            }
            for idx, item in enumerate(data)
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
