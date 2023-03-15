import dash_echarts
from dash import Dash, html

# https://echarts.apache.org/examples/en/index.html
# https://apache.github.io/echarts-handbook/en/concepts/style/
# https://echarts.apache.org/examples/en/editor.html?c=dataset-encode0


def main():
    app = Dash(__name__)

    option = {
        'dataset': {
            'source': [
                ['score', 'amount', 'product'],
                [89.3, 58212, 'Matcha Latte'],
                [57.1, 78254, 'Milk Tea'],
                [74.4, 41032, 'Cheese Cocoa'],
                [50.1, 12755, 'Cheese Brownie'],
                [89.7, 20145, 'Matcha Cocoa'],
                [68.1, 79146, 'Tea'],
                [19.6, 91852, 'Orange Juice'],
                [10.6, 101852, 'Lemon Juice'],
                [32.7, 20112, 'Walnut Brownie']
            ]
        },
        'grid': {'containLabel': True},
        'xAxis': {'name': 'amount'},
        'yAxis': {'type': 'category'},
        'visualMap': {
            'orient': 'horizontal',
            'left': 'center',
            'min': 10,
            'max': 100,
            'text': ['High Score', 'Low Score'],
            # Map the score column to color
            'dimension': 0,
            'inRange': {
                'color': ['#65B581', '#FFCE34', '#FD665F']
            }
        },
        'series': [
            {
                'type': 'bar',
                'encode': {
                    # Map the "product" column to X axis
                    'x': 'amount',
                    # Map the "product" column to Y axis
                    'y': 'product'
                }
            }
        ]
    }

    app.layout = html.Div(
        children=[
            dash_echarts.DashECharts(
                option=option,
                id='echarts',
                style={
                    "width": '98',
                    "height": '98',
                }
            ),
        ]
    )

    app.run_server(debug=False)


if __name__ == '__main__':

    main()
