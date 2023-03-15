import dash_echarts
from dash import Dash, html
from math import floor
from random import random
from datetime import datetime, timedelta

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=calendar-graph


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
        ['2017-03-14', 985]
    ]
    links = [
        {
            'source': idx,
            'target': idx + 1
        } for idx, item in enumerate(graphData)
    ]
    links.pop()

    option = {
        'tooltip': {},
        'calendar': {
            'top': 'middle',
            'left': 'center',
            'orient': 'vertical',
            'cellSize': 40,
            'yearLabel': {
                'margin': 50,
                'fontSize': 30
            },
            'dayLabel': {
                'firstDay': 1,
                'nameMap': 'cn'
            },
            'monthLabel': {
                'nameMap': 'cn',
                'margin': 15,
                'fontSize': 20,
                'color': '#999'
            },
            'range': ['2017-02', '2017-03-31']
        },
        'visualMap': {
            'min': 0,
            'max': 1000,
            'type': 'piecewise',
            'left': 'center',
            'bottom': 20,
            'inRange': {
                'color': ['#5291FF', '#C7DBFF']
            },
            'seriesIndex': [1],
            'orient': 'horizontal'
        },
        'series': [
            {
                'type': 'graph',
                'edgeSymbol': ['none', 'arrow'],
                'coordinateSystem': 'calendar',
                'links': links,
                'symbolSize': 15,
                'calendarIndex': 0,
                'itemStyle': {
                    'color': 'yellow',
                    'shadowBlur': 9,
                    'shadowOffsetX': 1.5,
                    'shadowOffsetY': 3,
                    'shadowColor': '#555'
                },
                'lineStyle': {
                    'color': '#D10E00',
                    'width': 1,
                    'opacity': 1
                },
                'data': graphData,
                'z': 20
            },
            {
                'type': 'heatmap',
                'coordinateSystem': 'calendar',
                'data': getVirtualData(2017)
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
            ),
        ]
    )

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
