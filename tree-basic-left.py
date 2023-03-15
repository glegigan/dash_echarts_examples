import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html
from json import load

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=tree-basic-left


def main():
    app = Dash(__name__)

    filepath = './static/flare.json'
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
                'top': '1%',
                'left': '15%',
                'bottom': '1%',
                'right': '7%',
                'symbolSize': 7,
                'orient': 'RL',
                'label': {
                    'position': 'left',
                    'verticalAlign': 'middle',
                    'align': 'left',
                    'fontSize': 9
                },
                'leaves': {
                    'label': {
                        'position': 'right',
                        'verticalAlign': 'middle',
                        'align': 'right'
                    }
                },
                'emphasis': {
                    'focus': 'descendant'
                },
                'expandAndCollapse': True,
                'animationDuration': 550,
                'animationDurationUpdate': 750
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
