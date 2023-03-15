import dash_echarts
from dash import Dash, html
from math import floor
from random import random
from datetime import datetime, timedelta

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=calendar-heatmap


def getVirtualData(year):
    startDate = datetime.strptime(str(year) + '-01-01', '%Y-%m-%d')
    endDate = datetime.strptime(str(year+1) + '-01-01', '%Y-%m-%d')
    date_generated = [startDate + timedelta(days=x) for x in range(0, (endDate - startDate).days)]
    data = []
    for time in date_generated:
        data.append(
            [
                time.strftime('%Y-%m-%d'), floor(random() * 1000)
            ]
        )
    return data


def main():
    app = Dash(__name__)

    option = {
      'title': {
        'top': 30,
        'left': 'center',
        'text': 'Daily Step Count'
      },
      'tooltip': {},
      'visualMap': {
        'min': 0,
        'max': 1000,
        'type': 'piecewise',
        'orient': 'horizontal',
        'left': 'center',
        'top': 65
      },
      'calendar': {
        'top': 120,
        'left': 30,
        'right': 30,
        'cellSize': ['auto', 13],
        'range': '2016',
        'itemStyle': {
          'borderWidth': 0.5
        },
        'yearLabel': {'show': False}
      },
      'series': {
        'type': 'heatmap',
        'coordinateSystem': 'calendar',
        'data': getVirtualData(2016)
      }
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
            ),
        ]
    )

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
