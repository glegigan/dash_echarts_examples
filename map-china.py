import dash_echarts
from dash import Dash, html, Input, Output
from os import path
import json


def main():
    app = Dash(__name__)

    option = {
        'title': {
            'text': '中国地图测试',
            'subtext': '中国地图测试',
            'sublink': 'localhost:8050'
        },
        'tooltip': {
            'trigger': 'item',
            'formatter': '{b}<br/>{c}'
        },
        'toolbox': {
            'show': True,
            'orient': 'vertical',
            'left': 'right',
            'top': 'center',
            'feature': {
                'dataView': {'readOnly': False},
                'restore': {},
                'saveAsImage': {}
            }
        },
        'visualMap': {
            'min': 0,
            'max': 200,
            'text': ['High', 'Low'],
            'realtime': False,
            'calculable': True,
            'inRange': {
                'color': ['lightskyblue', 'yellow', 'orangered']
            }
        },
        'series': [
            {
                'name': '中国地图测试',
                'type': 'map',
                'mapType': 'china',
                'label': {
                    'show': True
                },
                'data': [
                    {'name': '河南省', 'value': 16.7},
                    {'name': '上海市', 'value': 0.634050},
                    {'name': '北京市', 'value': 1.641054},
                    {'name': '广东省', 'value': 17.972507},
                    {'name': '新疆维吾尔自治区', 'value': 166.4897},
                    {'name': '西藏自治区', 'value': 122.84},
                ],
            }
        ]
    }

    # events = ["click"]
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath+'/static', 'china.json'))

    with open(filepath) as json_file:
        china_map = json.load(json_file)

    app.layout = html.Div(
        [
            html.P("hello", id='output'),
            dash_echarts.DashECharts(
                option=option,
                id='echarts',
                style={
                    "width": '98vw',
                    "height": '98vh',
                },
                maps={
                    "china": china_map
                }
            ),
        ]
    )

    @app.callback(
        output=Output(component_id='output', component_property='children'),
        inputs=[
            Input(component_id='echarts', component_property='click_data')
        ]
    )
    def update(data):
        if data:
            return f"clicked: {data['name']}"
        return 'not clicked!'

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
