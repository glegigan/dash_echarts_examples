import dash_bootstrap_components as dbc
import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# Extenssion: https://github.com/ecomfe/echarts-liquidfill


def main():
    app = Dash(__name__)

    option = {
        'series': [
            {
                'type': 'liquidFill',
                'data': [0.6, 0.5, 0.4, 0.3]
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

    app.run_server(debug=True)


if __name__ == '__main__':
    main()
