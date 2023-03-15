import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html
import math

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=line-polar2


def main():
    app = Dash(__name__)

    data = []
    for ii in range(360):
        t = (ii / 180) * math.pi
        r = math.sin(2 * t) * math.cos(2 * t)
        data.append([r, ii])

    option = {
      'title': {
        'text': 'Two Value-Axes in Polar'
      },
      'legend': {
        'data': ['line']
      },
      'polar': {
        'center': ['50%', '54%']
      },
      'tooltip': {
        'trigger': 'axis',
        'axisPointer': {
          'type': 'cross'
        }
      },
      'angleAxis': {
        'type': 'value',
        'startAngle': 0
      },
      'radiusAxis': {
        'min': 0
      },
      'series': [
        {
          'coordinateSystem': 'polar',
          'name': 'line',
          'type': 'line',
          'showSymbol': False,
          'data': data
        }
      ],
      'animationDuration': 2000
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
                            'width': '98vw',
                            'height': '98vh',
                        }
                    ),
                ]
            ),
        ],
        style={
            "width": '98vw',
            "height": '98vh',
        }
    )

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
