import dash_echarts
import random
from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=bar-histogram


def gen_data():
    return [
        [random.uniform(0, 30), random.randint(0, 300)] for ii in range(32)
    ]


def main():
    app = Dash(__name__)

    option = {
        'dataset': [
            {
                'source': gen_data()
            },
            {
                'transform': {'type': 'ecStat:histogram'}
            },
            {
                'transform': {
                    'type': 'ecStat:histogram',
                    'print': True,
                    'config': {'dimensions': [1]}
                }
            }
        ],
        'tooltip': {},
        'grid': [
            {
                'top': '50%',
                'right': '50%'
            },
            {
                'bottom': '52%',
                'right': '50%',
            },
            {
                'top': '50%',
                'left': '52%'
            }
        ],
        'xAxis': [
            {
                'scale': True,
                'gridIndex': 0
            },
            {
                'type': 'category',
                'scale': True,
                'axisTick': {'show': False},
                'axisLabel': {'show': False},
                'axisLine': {'show': False},
                'gridIndex': 1
            },
            {
                'scale': True,
                'gridIndex': 2
            }
        ],
        'yAxis': [
            {
                'gridIndex': 0
            },
            {
                'gridIndex': 1
            },
            {
                'type': 'category',
                'axisTick': {'show': False},
                'axisLabel': {'show': False},
                'axisLine': {'show': False},
                'gridIndex': 2
            }
        ],
        'series': [
            {
                'name': 'origianl scatter',
                'type': 'scatter',
                'xAxisIndex': 0,
                'yAxisIndex': 0,
                'encode': {'tooltip': [0, 1]},
                'datasetIndex': 0
            },
            {
                'name': 'histogram',
                'type': 'bar',
                'xAxisIndex': 1,
                'yAxisIndex': 1,
                'barWidth': '99.3%',
                'label': {
                    'show': True,
                    'position': 'top'
                },
                'encode': {'x': 0, 'y': 1, 'itemName': 4},
                'datasetIndex': 1
            },
            {
                'name': 'histogram',
                'type': 'bar',
                'xAxisIndex': 2,
                'yAxisIndex': 2,
                'barWidth': '99.3%',
                'label': {
                    'show': True,
                    'position': 'right'
                },
                'encode': {'x': 1, 'y': 0, 'itemName': 4},
                'datasetIndex': 2
            }
        ]
    }

    app.layout = html.Div(
        [
            dash_echarts.DashECharts(
                option=option,
                id='echarts',
                style={
                    "width": '98vw',
                    "height": '98vh',
                }
            ),
            dcc.Interval(id="interval", interval=1 * 1000, n_intervals=0),
        ]
    )

    @app.callback(
        output=Output(component_id='echarts', component_property='option'),
        inputs=[
            Input(component_id='interval', component_property='n_intervals')
        ]
    )
    def update(n_intervals):
        if n_intervals == 0:
            raise PreventUpdate
        else:
            option['dataset'][0]['source'] = gen_data()
        return option

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
