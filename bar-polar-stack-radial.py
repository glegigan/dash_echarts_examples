import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=bar-polar-stack-radial


def main():
    app = Dash(__name__)

    width = 2048 // 2
    height = 1176 // 2
    r = 480

    option = {
        'angleAxis': {
            'type': 'category',
            'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        'radiusAxis': {},
        'polar': {},
        'series': [
            {
                'type': 'bar',
                'data': [1, 2, 3, 4, 3, 5, 1],
                'coordinateSystem': 'polar',
                'name': 'A',
                'stack': 'a',
                'itemStyle': {
                    'global': True,
                    'type': 'radial',
                    'x': width,
                    'y': height,
                    'r': 20,
                    'colorStops': [
                        {'offset': .4, 'color': 'rgb(84, 112, 198)'.replace(')', ',.9)')},
                        {'offset': .6, 'color': 'rgb(84, 112, 198)'.replace(')', ',.8)')},
                        {'offset': .6, 'color': 'rgb(84, 112, 198)'}
                    ]
                },
                'emphasis': {
                    'focus': 'series'
                }
            },
            {
                'type': 'bar',
                'data': [2, 4, 6, 1, 3, 2, 1],
                'coordinateSystem': 'polar',
                'name': 'B',
                'stack': 'a',
                'itemStyle': {
                    'global': True,
                    'type': 'radial',
                    'x': width,
                    'y': height,
                    'r': 200,
                    'colorStops': [
                        {'offset': .4, 'color': 'rgb(145, 204, 117)'.replace(')', ',.9)')},
                        {'offset': .6, 'color': 'rgb(145, 204, 117)'.replace(')', ',.8)')},
                        {'offset': .9, 'color': 'rgb(145, 204, 117)'}
                    ]
                },
                'emphasis': {
                    'focus': 'series'
                }
            },
            {
                'type': 'bar',
                'data': [1, 2, 3, 4, 1, 2, 5],
                'coordinateSystem': 'polar',
                'name': 'C',
                'stack': 'a',
                'itemStyle': {
                    'global': True,
                    'type': 'radial',
                    'x': width,
                    'y': height,
                    'r': 400,
                    'colorStops': [
                        {'offset': .4, 'color': 'rgba(250, 199, 88)'.replace(')', ',.9)')},
                        {'offset': .6, 'color': 'rgba(250, 199, 88)'.replace(')', ',.8)')},
                        {'offset': .9, 'color': 'rgba(250, 199, 88)'}
                    ]
                },
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
        style={
            "width": '98vw',
            "height": '98vh',
        }
    )

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
