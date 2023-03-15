from os import getcwd
import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html
from json import load

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=tree-radial


def main():
    app = Dash(__name__)

    filepath = getcwd() + '/static/flare.json'
    with open(filepath) as json_file:
        data = load(json_file)

    option = {
        'tooltip': {
            'trigger': 'item',
            'triggerOn': 'mousemove'
        },
        'series': [
            {
                'type': 'tree',
                'data': [data],
                'top': '18%',
                'bottom': '14%',
                'layout': 'radial',
                'symbol': 'emptyCircle',
                'symbolSize': 7,
                'initialTreeDepth': 3,
                'animationDurationUpdate': 750,
                'emphasis': {
                    'focus': 'descendant'
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
