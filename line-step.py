import random

import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=line-step


def gen_randlist(num):
    return random.sample(range(num), 7)


def main():
    app = Dash(__name__)

    option = {
      'title': {
        'text': 'Step Line'
      },
      'tooltip': {
        'trigger': 'axis'
      },
      'legend': {
        'data': ['Step Start', 'Step Middle', 'Step End']
      },
      'grid': {
        'left': '3%',
        'right': '4%',
        'bottom': '3%',
        'containLabel': True
      },
      'toolbox': {
        'feature': {
          'saveAsImage': {}
        }
      },
      'xAxis': {
        'type': 'category',
        'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
      },
      'yAxis': {
        'type': 'value'
      },
      'series': [
        {
          'name': 'Step Start',
          'type': 'line',
          'step': 'start',
          'data': [120, 132, 101, 134, 90, 230, 210]
        },
        {
          'name': 'Step Middle',
          'type': 'line',
          'step': 'middle',
          'data': [220, 282, 201, 234, 290, 430, 410]
        },
        {
          'name': 'Step End',
          'type': 'line',
          'step': 'end',
          'data': [450, 432, 401, 454, 590, 530, 510]
        }
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
