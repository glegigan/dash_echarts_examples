import dash_echarts
from dash import Dash, html
from math import floor
from random import random
from datetime import datetime, timedelta

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=calendar-vertical


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
      'tooltip': {
        'position': 'top',
        'formatter': 'formatterTooltip',
      },
      'visualMap': {
        'min': 0,
        'max': 1000,
        'calculable': True,
        'orient': 'vertical',
        'left': '670',
        'top': 'center'
      },
      'calendar': [
        {
          'orient': 'vertical',
          'range': '2015'
        },
        {
          'left': 300,
          'orient': 'vertical',
          'range': '2016'
        },
        {
          'left': 520,
          'cellSize': [20, 'auto'],
          'bottom': 10,
          'orient': 'vertical',
          'range': '2017',
          'dayLabel': {
            'margin': 5
          }
        }
      ],
      'series': [
        {
          'type': 'heatmap',
          'coordinateSystem': 'calendar',
          'calendarIndex': 0,
          'data': getVirtualData(2015)
        },
        {
          'type': 'heatmap',
          'coordinateSystem': 'calendar',
          'calendarIndex': 1,
          'data': getVirtualData(2016)
        },
        {
          'type': 'heatmap',
          'coordinateSystem': 'calendar',
          'calendarIndex': 2,
          'data': getVirtualData(2017)
        }
      ]
    }

    app.layout = html.Div(
        children=[
            dash_echarts.DashECharts(
                option=option,
                # fun_keys=['formatter'],
                fun_values=['fm'],
                funs={
                    'formatterTooltip': '''
                    function (p) {
                      const format = echarts.time.format(p.data[0], '{yyyy}-{MM}-{dd}', false);
                      return format + ': ' + p.data[1];
                    }
                '''
                },
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
