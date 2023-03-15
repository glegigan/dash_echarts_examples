import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=pie-nest


def main():
    app = Dash(__name__)

    width = 2048 // 2
    height = 1176 // 2

    option = {
        'tooltip': {
            'trigger': 'item',
            'formatter': '{a} <br/>{b}: {c} ({d}%)'
        },
        'legend': {
            'data': [
                'Direct',
                'Marketing',
                'Search Engine',
                'Email',
                'Union Ads',
                'Video Ads',
                'Baidu',
                'Google',
                'Bing',
                'Others'
            ]
        },
        'series': [
            {
                'name': 'Access From',
                'type': 'pie',
                'selectedMode': 'single',
                'radius': [0, '30%'],
                'itemStyle': {
                    'borderRadius': 10,
                    'borderColor': '#fff',
                    'borderWidth': 2,
                },
                'label': {
                    'position': 'inner',
                    'fontSize': 14
                },
                'labelLine': {
                    'show': False
                },
                'data': [
                    {
                        'value': 1548,
                        'name': 'Search Engine',
                        'itemStyle': {
                            'global': True,
                            'type': 'radial',
                            'x': width,
                            'y': height,
                            'r': 20,
                            'colorStops': [
                                {'offset': .4, 'color': 'rgb(84, 112, 198)'.replace(')', ',.9)')},
                                {'offset': .6, 'color': 'rgb(84, 112, 198)'.replace(')', ',.8)')},
                                {'offset': .6, 'color': 'rgb(84, 112, 198)'}
                            ]
                        }
                    },
                    {
                        'value': 775,
                        'name': 'Direct',
                        'itemStyle': {
                            'global': True,
                            'type': 'radial',
                            'x': width,
                            'y': height,
                            'r': 20,
                            'colorStops': [
                                {'offset': .4, 'color': 'rgb(145, 204, 117)'.replace(')', ',.9)')},
                                {'offset': .6, 'color': 'rgb(145, 204, 117)'.replace(')', ',.8)')},
                                {'offset': .6, 'color': 'rgb(145, 204, 117)'}
                            ]
                        }
                    },
                    {
                        'value': 679,
                        'name': 'Marketing',
                        'selected': True,
                        'itemStyle': {
                            'global': True,
                            'type': 'radial',
                            'x': width,
                            'y': height,
                            'r': 20,
                            'colorStops': [
                                {'offset': .4, 'color': 'rgb((250, 199, 88)'.replace(')', ',.9)')},
                                {'offset': .6, 'color': 'rgb((250, 199, 88)'.replace(')', ',.8)')},
                                {'offset': .6, 'color': 'rgb((250, 199, 88)'}
                            ]
                        }
                    }
                ]
            },
            {
                'name': 'Access From',
                'type': 'pie',
                'radius': ['45%', '60%'],
                'labelLine': {
                    'length': 30
                },
                'label': {
                    'formatter': '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                    'backgroundColor': '#F6F8FC',
                    'borderColor': '#8C8D8E',
                    'borderWidth': 1,
                    'borderRadius': 4,
                    'rich': {
                        'a': {
                            'color': '#6E7079',
                            'lineHeight': 22,
                            'align': 'center'
                        },
                        'hr': {
                            'borderColor': '#8C8D8E',
                            'width': '100%',
                            'borderWidth': 1,
                            'height': 0
                        },
                        'b': {
                            'color': '#4C5058',
                            'fontSize': 14,
                            'fontWeight': 'bold',
                            'lineHeight': 33
                        },
                        'per': {
                            'color': '#fff',
                            'backgroundColor': '#4C5058',
                            'padding': [3, 4],
                            'borderRadius': 4
                        }
                    }
                },
                'data': [
                    {'value': 1048, 'name': 'Baidu'},
                    {'value': 335, 'name': 'Direct'},
                    {'value': 310, 'name': 'Email'},
                    {'value': 251, 'name': 'Google'},
                    {'value': 234, 'name': 'Union Ads'},
                    {'value': 147, 'name': 'Bing'},
                    {'value': 135, 'name': 'Video Ads'},
                    {'value': 102, 'name': 'Others'}
                ]
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
