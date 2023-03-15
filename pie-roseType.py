import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=pie-roseType


def main():
    app = Dash(__name__)

    option = {
        'title': {
            'text': 'Nightingale Chart',
            'subtext': 'Fake Data',
            'left': 'center'
        },
        'tooltip': {
            'trigger': 'item',
            'formatter': '{a} <br/>{b} : {c} ({d}%)'
        },
        'legend': {
            'left': 'center',
            'top': 'bottom',
            'data': [
                'rose1',
                'rose2',
                'rose3',
                'rose4',
                'rose5',
                'rose6',
                'rose7',
                'rose8'
            ]
        },
        'toolbox': {
            'show': True,
            'feature': {
                'mark': {'show': True},
                'dataView': {'show': True, 'readOnly': False},
                'restore': {'show': True},
                'saveAsImage': {'show': True}
            }
        },
        'series': [
            {
                'name': 'Radius Mode',
                'type': 'pie',
                'radius': [20, 340],
                'center': ['25%', '50%'],
                'roseType': 'radius',
                'itemStyle': {
                    'borderRadius': 5
                },
                'label': {
                    'show': False
                },
                'emphasis': {
                    'label': {
                        'show': True
                    }
                },
                'data': [
                    {'value': 40, 'name': 'rose 1'},
                    {'value': 33, 'name': 'rose 2'},
                    {'value': 28, 'name': 'rose 3'},
                    {'value': 22, 'name': 'rose 4'},
                    {'value': 20, 'name': 'rose 5'},
                    {'value': 15, 'name': 'rose 6'},
                    {'value': 12, 'name': 'rose 7'},
                    {'value': 10, 'name': 'rose 8'}
                ]
            },
            {
                'name': 'Area Mode',
                'type': 'pie',
                'radius': [20, 340],
                'center': ['75%', '50%'],
                'roseType': 'area',
                'itemStyle': {
                    'borderRadius': 5
                },
                'data': [
                    {'value': 30, 'name': 'rose 1'},
                    {'value': 28, 'name': 'rose 2'},
                    {'value': 26, 'name': 'rose 3'},
                    {'value': 24, 'name': 'rose 4'},
                    {'value': 22, 'name': 'rose 5'},
                    {'value': 20, 'name': 'rose 6'},
                    {'value': 18, 'name': 'rose 7'},
                    {'value': 16, 'name': 'rose 8'}
                ]
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
