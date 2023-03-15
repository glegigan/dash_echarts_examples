import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html, Input, Output, callback_context
from json import load
from dash.exceptions import PreventUpdate
from datetime import datetime
from time import mktime

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=line-race


filepath = './static/life-expectancy-table.json'
with open(filepath) as json_file:
    _rawData = load(json_file)


def get_countries():
    return list(set([e[3] for e in _rawData[1:]]))


dataset_with_filters = [
    {
        "id": f"dataset_{country}",
        "fromDatasetId": "dataset_raw",
        "transform": {
            "type": "filter",
            "config": {
                "and": [
                    {"dimension": "Year", "gte": 1950},
                    {"dimension": "Country", "=": country},
                ]
            },
        },
    }
    for country in get_countries()
]
series_list = [
    {
        "type": "line",
        "datasetId": f"dataset_{country}",
        "showSymbol": False,
        "name": country,
        "endLabel": {
            "show": True,
            "formatter": "line-raceFormatter"
        },
        "labelLayout": {"moveOverlap": "shiftY"},
        "emphasis": {"focus": "series"},
        "encode": {
            "x": "Year",
            "y": "Income",
            "label": ["Country", "Income"],
            "itemName": "Year",
            "tooltip": ["Income"],
        },
    }
    for country in get_countries()
]

option = {
    "animationDuration": 10000,
    "animation": True,
    "dataset": [
                   {"id": "dataset_raw", "source": _rawData}
               ] + dataset_with_filters,
    "title": {"text": "Income since 1950"},
    "tooltip": {"order": "valueDesc", "trigger": "axis"},
    "xAxis": {"type": "category", "nameLocation": "middle"},
    "yAxis": {"name": "Income"},
    "grid": {"right": 140},
    "series": series_list,
}

layout = html.Div(
    children=[
        dash_echarts.DashECharts(
            option=option,
            id='echarts',
            funs={
                "line-raceFormatter":
                    '''
                    function(params){ 
                        return params.value[3] + ': ' + params.value[0];
                    }
                    '''
            },
            fun_values=['line-raceFormatter'],
            style={
                "width": '98%',
                "height": '98vh',
            },
        ),
        dbc.Button(
            'restart',
            color='success',
            id='line-race-button',
            style={
                'position': 'absolute',
                'height': 50, 'width': '5%',
                'top': '10%', 'right': '80%',
                'opacity': 0.8
            }
        ),
    ]
)


def main():
    app = Dash(
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        meta_tags=[
            {"name": "viewport", "content": "width=device-width, initial-scale=1"}
        ],
        suppress_callback_exceptions=True,
    )

    app.layout = layout

    @app.callback(
        output=Output(component_id='echarts', component_property='reset_id'),
        inputs=[
            Input(component_id="line-race-button", component_property='n_clicks')
        ],
    )
    def update_line_race(n_clicks):
        triggered = callback_context.triggered
        # value = triggered[0]['value']
        prop_id, event = triggered[0]['prop_id'].split('.')
        if n_clicks:
            if 'line-race-button' in prop_id:
                dtime = datetime.now()
                int_time = int(mktime(dtime.timetuple()))
                return int_time
        raise PreventUpdate

    app.run_server(debug=False)


if __name__ == '__main__':
    main()
