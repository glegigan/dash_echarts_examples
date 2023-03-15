from random import random

import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html


# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=custom-bar-trend


def main():
    app = Dash(__name__)

    yearCount = 7
    categoryCount = 30
    xAxisData = []
    customData = []
    legendData = []
    dataList = []
    legendData.append('trend')
    encodeY = []

    for ii in range(yearCount):
        legendData.append(str(2010 + ii) + '')
        dataList.append([])
        encodeY.append(1 + ii)

    for ii in range(categoryCount):
        val = random() * 1000
        xAxisData.append('category' + str(ii))
        customVal = [ii]
        customData.append(customVal)
        for jj in range(len(dataList)):
            value = round(val, 2) if jj == 0 else round(max(0, dataList[jj - 1][ii] + (random() - 0.5) * 200), 2)
            dataList[jj].append(value)
            customVal.append(value)

    option = {
        'tooltip': {
            'trigger': 'axis'
        },
        'legend': {
            'data': legendData
        },
        'dataZoom': [
            {
                'type': 'slider',
                'start': 50,
                'end': 70
            },
            {
                'type': 'inside',
                'start': 50,
                'end': 70
            }
        ],
        'xAxis': {
            'data': xAxisData
        },
        'yAxis': {},
        'series': [
              {
                  'type': 'custom',
                  'name': 'trend',
                  'renderItem': 'ri',
                  'itemStyle': {
                      'borderWidth': 2
                  },
                  'encode': {
                      'x': 0,
                      'y': encodeY
                  },
                  'data': customData,
                  'z': 100
              },
          ] +
          [
              {
                  'type': 'bar',
                  'animation': False,
                  'name': legendData[index + 1],
                  'itemStyle': {
                      'opacity': 0.5
                  },
                  'data': data
              } for index, data in enumerate(dataList)
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
                        fun_keys=['renderItem'],
                        funs={
                            'ri': '''
                            function (params, api) {
                                var xValue = api.value(0);
                                var currentSeriesIndices = api.currentSeriesIndices();
                                var barLayout = api.barLayout({
                                  barGap: '30%',
                                  barCategoryGap: '20%',
                                  count: currentSeriesIndices.length - 1
                                });
                                var points = [];
                                for (var i = 0; i < currentSeriesIndices.length; i++) {
                                  var seriesIndex = currentSeriesIndices[i];
                                  if (seriesIndex !== params.seriesIndex) {
                                    var point = api.coord([xValue, api.value(seriesIndex)]);
                                    point[0] += barLayout[i - 1].offsetCenter;
                                    point[1] -= 20;
                                    points.push(point);
                                  }
                                }
                                var style = api.style({
                                  stroke: api.visual('color'),
                                  fill: 'none'
                                });
                                console.log(points)
                                return {
                                  type: 'polyline',
                                  shape: {
                                    points: points
                                  },
                                  style: style
                                };
                              }
                            '''
                        },
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
