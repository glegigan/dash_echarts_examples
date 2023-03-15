import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=bar-y-category-stack


def main():
    app = Dash(__name__)

    option = {
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': {
                'type': 'shadow'    # line' or 'shadow'
            }
        },
        'grid': {
            'left': '3%',
            'right': '4%',
            'bottom': '3%',
            'containLabel': True,
            'show': False,
            'z': 0,
            'top': 60,
            'backgroundColor': 'rgba(0, 0, 0, 0)',
            'borderWidth': 1,
            'borderColor':  '#ccc',
        },
        'xAxis': {
            'type': 'value'
        },
        'yAxis': {
            'type': 'category',
            'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        'series': [
            {
                'name': 'Direct',
                'type': 'bar',
                'stack': 'total',
                'label': {
                    'show': True
                },
                'emphasis': {
                    'focus': 'series'
                },
                'data': [320, 302, 301, 334, 390, 330, 320]
            },
            {
                'name': 'Mail Ad',
                'type': 'bar',
                'stack': 'total',
                'label': {
                    'show': True
                },
                'emphasis': {
                    'focus': 'series'
                },
                'data': [120, 132, 101, 134, 90, 230, 210]
            },
            {
                'name': 'Affiliate Ad',
                'type': 'bar',
                'stack': 'total',
                'label': {
                    'show': True
                },
                'emphasis': {
                    'focus': 'series'
                },
                'data': [220, 182, 191, 234, 290, 330, 310]
            },
            {
                'name': 'Video Ad',
                'type': 'bar',
                'stack': 'total',
                'label': {
                    'show': True
                },
                'emphasis': {
                    'focus': 'series'
                },
                'data': [150, 212, 201, 154, 190, 330, 410]
            },
            {
                'name': 'Search Engine',
                'type': 'bar',
                'stack': 'total',
                'label': {
                    'show': True
                },
                'emphasis': {
                    'focus': 'series'
                },
                'data': [820, 832, 901, 934, 1290, 1330, 1320]
            }
        ],
        'legend': {},
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
