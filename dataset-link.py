import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html, Input, Output
from dash.exceptions import PreventUpdate


# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=custom-polar-heatmap


dataset = [
    ['product', '2012', '2013', '2014', '2015', '2016', '2017'],
    ['Milk Tea', 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
    ['Matcha Latte', 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
    ['Cheese Cocoa', 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
    ['Walnut Brownie', 25.2, 37.1, 41.2, 18, 33.9, 49.1]
]


def main():
    app = Dash(__name__)

    option = {
        'legend': {},
        'tooltip': {
          'trigger': 'axis',
          'showContent': False
        },
        'dataset': {
          'source': dataset,
        },
        'xAxis': {'type': 'category'},
        'yAxis': {'gridIndex': 0},
        'grid': {'top': '55%'},
        'series': [
          {
            'type': 'line',
            'smooth': True,
            'seriesLayoutBy': 'row',
            'emphasis': {'focus': 'series'}
          },
          {
            'type': 'line',
            'smooth': True,
            'seriesLayoutBy': 'row',
            'emphasis': {'focus': 'series' }
          },
          {
            'type': 'line',
            'smooth': True,
            'seriesLayoutBy': 'row',
            'emphasis': {'focus': 'series'}
          },
          {
            'type': 'line',
            'smooth': True,
            'seriesLayoutBy': 'row',
            'emphasis': {'focus': 'series' }
          },
          {
            'type': 'pie',
            'id': 'pie',
            'radius': '30%',
            'center': ['50%', '25%'],
            'emphasis': {
              'focus': 'self'
            },
            'label': {
              'formatter': '{b}: {@2012} ({d}%)'
            },
            'encode': {
              'itemName': 'product',
              'value': '2012',
              'tooltip': '2012'
            }
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
                            'width': '98vw',
                            'height': '98vh',
                        }
                    ),
                ]
            ),
        ],
    )

    @app.callback(
        output=Output(component_id='echarts', component_property='option'),
        inputs=[
            Input(component_id='echarts', component_property='axis_pointer_data')
        ]
    )
    def update(event):
        if event and 'axesInfo' in event and event['axesInfo'] != []:
            xAxisInfo = event['axesInfo'][0]
            dimension = dataset[0][xAxisInfo['value'] + 1]
            option['series'][4] = {
                'type': 'pie',
                'id': 'pie',
                'radius': '30%',
                'center': ['50%', '25%'],
                'emphasis': {
                    'focus': 'self'
                },
                'label': {
                    'formatter': '{b}: {@[' + dimension + ']} ({d}%)'
                },
                'encode': {
                    'itemName': 'product',
                    'value': dimension,
                    'tooltip': dimension
                }
            }
            return option
        else:
            raise PreventUpdate

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
