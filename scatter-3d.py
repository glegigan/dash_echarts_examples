import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, dcc, Input, Output
from os import getcwd
import json

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=scatter3D-dataset&gl=1


def main():
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    filepath = getcwd() + '/static/life-expectancy-table.json'
    with open(filepath) as json_file:
        data = json.load(json_file)

    option = {
        'grid3D': {},
        'xAxis3D': {
            'type': 'category',
            'axisLabel': {
                'interval': 0,
                'rotate': 45
            },
        },
        'yAxis3D': {
            'min': 1750,
            'max': 2050
        },
        'zAxis3D': {
            'min': 0,
            'max': 100
        },
        'dataset': {
            'dimensions': [
                {'name': 'Income', 'type': 'int'},
                {'name': 'Life', 'type': 'int'},
                {'name': 'Population', 'type': 'int'},
                {'name': 'Country', 'type': 'ordinal'},
                {'name': 'Year', 'type': 'int'}
            ],
            'source': data
        },
        'series': [
            {
                'type': 'scatter3D',
                'symbolSize': 6,
                'encode': {
                    'x': 'Country',
                    'y': 'Year',
                    'z': 'Income',
                    'tooltip': [0, 1, 2, 3, 4]
                }
            },
        ]
    }
    dropdowns = ['Income', 'Life', 'Population', 'Country', 'Year']
    controls = dbc.Card(
        children=[
            dbc.Row(
                children=[
                    dbc.Label("X"),
                    dcc.Dropdown(
                        id="x",
                        options=[
                            {"label": col, "value": col} for col in dropdowns
                        ],
                        value="Country",
                    ),
                ],
            ),
            dbc.Row(
                children=[
                    dbc.Label("Y"),
                    dcc.Dropdown(
                        id="y",
                        options=[
                            {"label": col, "value": col} for col in dropdowns
                        ],
                        value="Year",
                    ),
                ],
            ),
            dbc.Row(
                children=[
                    dbc.Label("Z"),
                    dcc.Dropdown(
                        id="z",
                        options=[
                            {"label": col, "value": col} for col in dropdowns
                        ],
                        value="Life",
                    ),
                ]
            ),
        ],
        body=True,
        style={
            'position': 'absolute',
            'height': 300, 'width': 300,
            'top': 150, 'left': 150
        }
    )

    app.layout = dbc.Container(
        [
            dbc.Row(
                [
                    dash_echarts.DashECharts(
                        option=option,
                        id='echarts',
                        style={
                            "width": '100vw',
                            "height": '80vh',
                        }
                    ),
                ]
            ),
            controls,
        ],
        fluid=True,
    )

    def setup_axis(option, an, v):
        if v == 'Country':
            option[an] = {
                'type': 'category',
                'axisLabel': {
                    'interval': 0,
                    'rotate': 45
                },
            }
        elif v == 'Year':
            option[an] = {
                'type': 'value',
                'min': 1750,
                'max': 2050
            }
        elif v == 'Income':
            option[an] = {
                'type': 'value',
                'min': 0,
                'max': 80000
            }
        elif v == 'Population':
            option[an] = {
                'type': 'value',
                'min': 0,
                'max': 2000000000
            }
        elif v == 'Life':
            option[an] = {
                'type': 'value',
                'min': 0,
                'max': 100
            }

    @app.callback(
        output=Output('echarts', 'option'),
        inputs=[
            Input(component_id='x', component_property='value'),
            Input(component_id='y', component_property='value'),
            Input(component_id='z', component_property='value')
        ]
    )
    def update(x, y, z):
        option['series'][0]['encode']['x'] = x
        option['series'][0]['encode']['y'] = y
        option['series'][0]['encode']['z'] = z

        setup_axis(option, 'xAxis3D', x)
        setup_axis(option, 'yAxis3D', y)
        setup_axis(option, 'zAxis3D', z)

        return option

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
