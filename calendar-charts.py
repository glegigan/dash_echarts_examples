import dash_echarts
from dash import Dash, html
from math import floor
from random import random
from datetime import datetime, timedelta

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=calendar-charts


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

    graphData = [
        ['2017-02-01', 260],
        ['2017-02-04', 200],
        ['2017-02-09', 279],
        ['2017-02-13', 847],
        ['2017-02-18', 241],
        ['2017-02-23', 411],
        ['2017-02-27', 985]
    ]
    links = [
        {
            'source': idx,
            'target': idx + 1
        } for idx, item in enumerate(graphData)
    ]
    links.pop()

    option = {
        'tooltip': {
            'position': 'top'
        },
        'visualMap': [
            {
                'min': 0,
                'max': 1000,
                'calculable': True,
                'seriesIndex': [2, 3, 4],
                'orient': 'horizontal',
                'left': '55%',
                'bottom': 20
            },
            {
                'min': 0,
                'max': 1000,
                'inRange': {
                    'color': ['grey'],
                    'opacity': [0, 0.3]
                },
                'controller': {
                    'inRange': {
                        'opacity': [0.3, 0.6]
                    },
                    'outOfRange': {
                        'color': '#ccc'
                    }
                },
                'seriesIndex': [1],
                'orient': 'horizontal',
                'left': '10%',
                'bottom': 20
            }
        ],
        'calendar': [
            {
                'orient': 'vertical',
                'yearLabel': {
                    'margin': 40
                },
                'monthLabel': {
                    'nameMap': 'cn',
                    'margin': 20
                },
                'dayLabel': {
                    'firstDay': 1,
                    'nameMap': 'cn'
                },
                'cellSize': 40,
                'range': '2017-02'
            },
            {
                'orient': 'vertical',
                'yearLabel': {
                    'margin': 40
                },
                'monthLabel': {
                    'margin': 20
                },
                'cellSize': 40,
                'left': 460,
                'range': '2017-01'
            },
            {
                'orient': 'vertical',
                'yearLabel': {
                    'margin': 40
                },
                'monthLabel': {
                    'margin': 20
                },
                'cellSize': 40,
                'top': 350,
                'range': '2017-03'
            },
            {
                'orient': 'vertical',
                'yearLabel': {
                    'margin': 40
                },
                'dayLabel': {
                    'firstDay': 1,
                    'nameMap': ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
                },
                'monthLabel': {
                    'nameMap': 'cn',
                    'margin': 20
                },
                'cellSize': 40,
                'top': 350,
                'left': 460,
                'range': '2017-04'
            }
        ],
        'series': [
            {
                'type': 'graph',
                'edgeSymbol': ['none', 'arrow'],
                'coordinateSystem': 'calendar',
                'links': links,
                'symbolSize': 10,
                'calendarIndex': 0,
                'data': graphData
            },
            {
                'type': 'heatmap',
                'coordinateSystem': 'calendar',
                'data': getVirtualData(2017)
            },
            {
                'type': 'effectScatter',
                'coordinateSystem': 'calendar',
                'calendarIndex': 1,
                'symbolSize': 'symbolSize1',
                'data': getVirtualData(2017)
            },
            {
                'type': 'scatter',
                'coordinateSystem': 'calendar',
                'calendarIndex': 2,
                'symbolSize': 'symbolSize2',
                'data': getVirtualData(2017),
            },
            {
                'type': 'heatmap',
                'coordinateSystem': 'calendar',
                'calendarIndex': 3,
                'data': getVirtualData(2017)
            }
        ]
    }

    app.layout = html.Div(
        children=[
            dash_echarts.DashECharts(
                option=option,
                id='echarts',
                fun_keys=['symbolSize', 'symbolSize'],
                funs={
                    'symbolSize1': '''
                        function (val) {
                        return val[1] / 40;
                      }
                    ''',
                    'symbolSize2': '''
                        function (val) {
                        return val[1] / 60;
                    }
                ''',
                },
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
