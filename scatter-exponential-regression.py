import random
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=scatter-exponential-regression


def gen_data():
    return [
        [random.uniform(0, 30), random.randint(0, 300)] for ii in range(32)
    ]


def main():
    app = Dash(__name__)

    option = {
        'dataset': [
            {
                'source': [
                    [1, 4862.4],
                    [2, 5294.7],
                    [3, 5934.5],
                    [4, 7171.0],
                    [5, 8964.4],
                    [6, 10202.2],
                    [7, 11962.5],
                    [8, 14928.3],
                    [9, 16909.2],
                    [10, 18547.9],
                    [11, 21617.8],
                    [12, 26638.1],
                    [13, 34634.4],
                    [14, 46759.4],
                    [15, 58478.1],
                    [16, 67884.6],
                    [17, 74462.6],
                    [18, 79395.7]
                ]
            },
            {
                'transform': {
                    'type': 'ecStat:regression',
                    'config': {
                        'method': 'exponential'
                    }
                }
            }
        ],
        'title': {
            'text': '1981 - 1998 gross domestic product GDP (trillion yuan)',
            'subtext': 'By ecStat.regression',
            'sublink': 'https://github.com/ecomfe/echarts-stat',
            'left': 'center'
          },
          'tooltip': {
            'trigger': 'axis',
            'axisPointer': {
              'type': 'cross'
            }
          },
          'xAxis': {
            'splitLine': {
              'lineStyle': {
                'type': 'dashed'
              }
            }
          },
          'yAxis': {
            'splitLine': {
              'lineStyle': {
                'type': 'dashed'
              }
            }
          },
          'series': [
            {
              'name': 'scatter',
              'type': 'scatter',
              'datasetIndex': 0
            },
            {
              'name': 'line',
              'type': 'line',
              'smooth': True,
              'datasetIndex': 1,
              'symbolSize': 0.1,
              'symbol': 'circle',
              'label': {'show': True, 'fontSize': 16},
              'labelLayout': {'dx': -20 },
              'encode': {'label': 2, 'tooltip': 1}
            }
          ]
        }

    app.layout = html.Div(
        children=[
            dash_echarts.DashECharts(
                option=option,
                id='echarts',
                style={
                    "width": '98vw',
                    "height": '98vh',
                }
            )
        ]
    )
    app.run_server(debug=False)


if __name__ == '__main__':
    main()
