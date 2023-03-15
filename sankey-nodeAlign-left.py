import json
import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=sankey-nodeAlign-right


def main():
    app = Dash(__name__)

    with open('./static/energy.json') as f:
        data = json.load(f)

    option = {
        'title': {
            'text': 'Node Align Right'
        },
        'tooltip': {
            'trigger': 'item',
            'triggerOn': 'mousemove'
        },
        'animation': True,
        'series': [
            {
                'type': 'sankey',
                'emphasis': {
                    'focus': 'adjacency'
                },
                'nodeAlign': 'left',
                'data': data['nodes'],
                'links': data['links'],
                'lineStyle': {
                    'color': 'source',
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
