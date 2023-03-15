import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=radar2


def generateLegend():
    lst = []
    for ii in range(0, 28):
        lst.append(str(ii + 2000))
    return lst


def generateSeries():
    series = []
    for ii in range(0, 28):
        series.append(
            {
                'type': 'radar',
                'symbol': 'none',
                'lineStyle': {
                    'width': 1
                },
                'emphasis': {
                    'areaStyle': {
                        'color': 'rgba(0,250,0,0.3)'
                    }
                },
                'data': [
                    {
                        'value': [
                            (40 - ii) * 10,
                            (38 - ii) * 4 + 60,
                            ii * 5 + 10,
                            ii * 9,
                            (ii * ii) / 2
                        ],
                        'name': str(ii + 2000)
                    }
                ]
            }
        )
    return series


def main():
    app = Dash(__name__)

    option = {
        'title': {
            'text': 'Proportion of Browsers',
            'subtext': 'Fake Data',
            'top': 10,
            'left': 10
        },
        'tooltip': {
            'trigger': 'item'
        },
        'legend': {
            'type': 'scroll',
            'bottom': 10,
            'data': generateLegend(),
        },
        'visualMap': {
            'top': 'middle',
            'right': 10,
            'color': ['red', 'yellow'],
            'calculable': True
        },
        'radar': {
            'indicator': [
                {'text': 'IE8-', 'max': 400},
                {'text': 'IE9+', 'max': 400},
                {'text': 'Safari', 'max': 400},
                {'text': 'Firefox', 'max': 400},
                {'text': 'Chrome', 'max': 400}
            ]
        },
        'series': generateSeries(),
    }

    app.layout = html.Div([
        dash_echarts.DashECharts(
            option=option,
            id='echarts',
            style={
                "width": '98vw',
                "height": '98vh',
            }
        ),
    ])
    app.run_server(debug=False)


if __name__ == '__main__':
    main()
