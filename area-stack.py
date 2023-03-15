import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=area-stack


def main():
    app = Dash(__name__)

    option = {
        'color': ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', 'fc8452', '#9a60b4', '#ea7ccc'],
        'title': {'text': '堆叠区域图'},
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': {'type': 'cross', 'label': {'backgroundColor': '#6a7985'}},
        },
        'legend': {'data': ['邮件营销', '联盟广告', '视频广告', '直接访问', '搜索引擎']},
        'toolbox': {'feature': {'saveAsImage': {}}},
        'grid': {'left': '3%', 'right': '4%', 'bottom': '3%', 'containLabel': True},
        'xAxis': [
            {
                'type': 'category',
                'boundaryGap': False,
                'data': ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
            }
        ],
        'yAxis': [{'type': 'value'}],
        'series': [
            {
                'name': '邮件营销',
                'type': 'line',
                'stack': '总量',
                'areaStyle': {
                    'opacity': 0.8,
                    'color': {
                        'colorStops': [
                            {'offset': 0, 'color': '#91cc75'},
                            {'offset': 1, 'color': '#5470c6'},
                        ],
                        'x': 0,
                        'y': 0,
                        'x2': 0,
                        'y2': 1,
                        'type': 'radial',
                        'global': False,
                    },
                },
                'emphasis': {'focus': 'series'},
                'data': [120, 132, 101, 134, 90, 230, 210],
            },
            {
                'name': '联盟广告',
                'type': 'line',
                'stack': '总量',
                'areaStyle': {
                    'opacity': 0.8,
                    'color': {
                        'colorStops': [
                            {'offset': 0, 'color': '#fac858'},
                            {'offset': 1, 'color': '#91cc75'},
                        ],
                        'x': 0,
                        'y': 0,
                        'x2': 0,
                        'y2': 1,
                        'type': 'radial',
                        'global': False,
                    },
                },
                'emphasis': {'focus': 'series'},
                'data': [220, 182, 191, 234, 290, 330, 310],
            },
            {
                'name': '视频广告',
                'type': 'line',
                'stack': '总量',
                'areaStyle': {
                    'opacity': 0.8,
                    'color': {
                        'colorStops': [
                            {'offset': 0, 'color': '#ee6666'},
                            {'offset': 1, 'color': '#fac858'},
                        ],
                        'x': 0,
                        'y': 0,
                        'x2': 0,
                        'y2': 1,
                        'type': 'radial',
                        'global': False,
                    }
                },
                'emphasis': {'focus': 'series'},
                'data': [150, 232, 201, 154, 190, 330, 410],
            },
            {
                'name': '直接访问',
                'type': 'line',
                'stack': '总量',
                'areaStyle': {
                    'opacity': 0.8,
                    'color': {
                        'colorStops': [
                            {'offset': 0, 'color': '#73c0de'},
                            {'offset': 1, 'color': '#ee6666'},
                        ],
                        'x': 0,
                        'y': 0,
                        'x2': 0,
                        'y2': 1,
                        'type': 'radial',
                        'global': False,
                    },
                },
                'emphasis': {'focus': 'series'},
                'data': [320, 332, 301, 334, 390, 330, 320],
            },
            {
                'name': '搜索引擎',
                'type': 'line',
                'stack': '总量',
                'label': {'show': True, 'position': 'top'},
                'areaStyle': {
                    'opacity': 0.8,
                    'color': {
                        'colorStops': [
                            {'offset': 0, 'color': '#3ba272'},
                            {'offset': 1, 'color': '#73c0de'},
                        ],
                        'x': 0,
                        'y': 0,
                        'x2': 0,
                        'y2': 1,
                        'type': 'radial',
                        'global': False,
                    },
                },
                'emphasis': {'focus': 'series'},
                'data': [820, 932, 901, 934, 1290, 1330, 1320],
            },
        ],
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

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
