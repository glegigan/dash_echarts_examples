import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=bar-polar-stack


def main():
    app = Dash(__name__)

    option = {
        'angleAxis': {},
        'radiusAxis': {
            'type': 'category',
            'data': ['Mon', 'Tue', 'Wed', 'Thu'],
            'z': 10
        },
        'polar': {},
        'series': [
            {
                'type': 'bar',
                'data': [1, 2, 3, 4],
                'coordinateSystem': 'polar',
                'name': 'A',
                'stack': 'a',
                'emphasis': {
                    'focus': 'series'
                }
            },
            {
                'type': 'bar',
                'data': [2, 4, 6, 8],
                'coordinateSystem': 'polar',
                'name': 'B',
                'stack': 'a',
                'emphasis': {
                    'focus': 'series'
                }
            },
            {
                'type': 'bar',
                'data': [1, 2, 3, 4],
                'coordinateSystem': 'polar',
                'name': 'C',
                'stack': 'a',
                'emphasis': {
                    'focus': 'series'
                }
            }
        ],
        'legend': {
            'show': True,
            'data': ['A', 'B', 'C']
        }
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
