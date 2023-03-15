import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=pie-simple


def main():
    app = Dash(__name__)

    option = {
        'title': {
            'text': 'Referer of a Website',
            'subtext': 'Fake Data',
            'left': 'center'
        },
        'tooltip': {
            'trigger': 'item'
        },
        'legend': {
            'orient': 'vertical',
            'left': 'left'
        },
        'series': [
            {
                'name': 'Access From',
                'type': 'pie',
                'selectedMode': 'single',
                'selectedOffset': 30,
                'radius': '75%',
                'data': [
                    {'value': 1048, 'name': 'Search Engine'},
                    {'value': 735, 'name': 'Direct'},
                    {'value': 580, 'name': 'Email'},
                    {'value': 484, 'name': 'Union Ads'},
                    {'value': 300, 'name': 'Video Ads', 'selected': True}
                ],
                'emphasis': {
                    'itemStyle': {
                        'shadowBlur': 10,
                        'shadowOffsetX': 0,
                        'shadowColor': 'rgba(0, 0, 0, 0.5)'
                    }
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
                            'width': '100vw',
                            'height': '100vh',
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
