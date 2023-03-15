import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=pie-doughnut


def main():
    app = Dash(__name__)

    width = 2048 // 2
    height = 1176 // 2
    r = 480

    option = {
        'color': [
            'rgb(84, 112, 198)',
            'rgb(145, 204, 117)',
            'rgb(250, 199, 88)',
            'rgb(238, 102, 102)',
            'rgb(59, 162, 114)',
            'rgb(252, 133, 82)',
            'rgb(153, 96, 180)',
            'rgb(234, 124, 205)'
        ],
        'tooltip': {
            'trigger': 'item',
            'formatter': '{a} <br/>{b} : {c} ({d}%)'
        },
        'legend': {
            'orient': 'vertical',
            'left': 'left',
            'data': [
                'Direct Access',
                'Email Marketing',
                'Affiliate Ads',
                'Video Ads',
                'Search Engines'
            ]
        },
        'series': [
            {
                'name': 'Access Source',
                'type': 'pie',
                'radius': ['40%', '70%'],
                'center': ['50%', '50%'],
                # 'startAngle': 0,
                'avoidLabelOverlap': True,
                'itemStyle': {
                    'borderRadius': 10,
                    'borderColor': '#fff',
                    'borderWidth': 2,
                },
                'label': {
                    'show': True,
                    # 'position': 'center'
                },
                'data': [
                    {
                        'value': 335,
                        'name': 'Direct Access',
                        'itemStyle': {
                            'color': {
                                'global': True,
                                'type': 'radial',
                                'x': width,
                                'y': height,
                                'r': r,
                                'colorStops': [
                                    {'offset': .4, 'color': 'rgb(84, 112, 198)'.replace(')', ',.9)')},
                                    {'offset': .6, 'color': 'rgb(84, 112, 198)'.replace(')', ',.8)')},
                                    {'offset': .9, 'color': 'rgb(84, 112, 198)'}
                                ]
                            },
                        },
                    },
                    {
                        'value': 310,
                        'name': 'Email Marketing',
                        'itemStyle': {
                           'color': {
                                'global': True,
                                'type': 'radial',
                                'x': width,
                                'y': height,
                                'r': r,
                                'colorStops': [
                                    {'offset': .4, 'color': 'rgb(145, 204, 117)'.replace(')', ',.9)')},
                                    {'offset': .6, 'color': 'rgb(145, 204, 117)'.replace(')', ',.8)')},
                                    {'offset': .9, 'color': 'rgb(145, 204, 117)'}
                                ]
                            },
                        },
                    },
                    {
                        'value': 234,
                        'name': 'Affiliate Ads',
                        'itemStyle': {
                            'color': {
                                'global': True,
                                'type': 'radial',
                                'x': width,
                                'y': height,
                                'r': r,
                                'colorStops': [
                                    {'offset': .4, 'color': 'rgba(250, 199, 88)'.replace(')', ',.9)')},
                                    {'offset': .6, 'color': 'rgba(250, 199, 88)'.replace(')', ',.8)')},
                                    {'offset': .9, 'color': 'rgba(250, 199, 88)'}
                                ]
                            },
                        },
                    },
                    {
                        'value': 135,
                        'name': 'Video Ads',
                        'itemStyle': {
                            'color': {
                                'global': True,
                                'type': 'radial',
                                'x': width,
                                'y': height,
                                'r': r,
                                'colorStops': [
                                    {'offset': .4, 'color': 'rgba(238, 102, 102)'.replace(')', ',.9)')},
                                    {'offset': .6, 'color': 'rgba(238, 102, 102)'.replace(')', ',.8)')},
                                    {'offset': .9, 'color': 'rgba(238, 102, 102)'}
                                ]
                            },
                        },
                    },
                    {
                        'value': 1548,
                        'name': 'Search Engines',
                        'itemStyle': {
                            'color': {
                                'global': True,
                                'type': 'radial',
                                'x': width,
                                'y': height,
                                'r': r,
                                'colorStops': [
                                    {'offset': .4, 'color': 'rgb(59, 162, 114)'.replace(')', ',.9)')},
                                    {'offset': .6, 'color': 'rgb(59, 162, 114)'.replace(')', ',.8)')},
                                    {'offset': .9, 'color': 'rgb(59, 162, 114)'}
                                ]
                            },
                        },
                    }
                ],
                'emphasis': {
                    'label': {
                        'show': True,
                        'fontSize': 40,
                        'fontWeight': 'bold'
                    },
                    'itemStyle': {
                        'shadowBlur': 10,
                        'shadowOffsetX': 0,
                        'shadowColor': 'rgba(0, 0, 0, 0.5)'
                    }
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
