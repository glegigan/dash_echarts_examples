import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html
import json

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=graph-label-overlap


def main():
    app = Dash(__name__)

    with open('./static/les-miserables.json') as f:
        graph = json.load(f)

    option = {
        'tooltip': {},
        'legend': [
            {
                'data': [a['name'] for a in graph['categories']],
            }
        ],
        'series': [
            {
                'name': 'Les Miserables',
                'type': 'graph',
                'layout': 'none',
                'data': graph['nodes'],
                'links': graph['links'],
                'categories': graph['categories'],
                'roam': True,
                'label': {
                    'show': True,
                    'position': 'right',
                    'formatter': '{b}'
                },
                'labelLayout': {
                    'hideOverlap': True
                },
                'scaleLimit': {
                    'min': 0.4,
                    'max': 2
                },
                'lineStyle': {
                    'color': 'source',
                    'curveness': 0.3
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
