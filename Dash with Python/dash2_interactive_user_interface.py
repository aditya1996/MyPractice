import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Input(id='input', value='Enter Something', type='text'),
    dcc.Output
    ])


if __name__ == "__main__":
    app.run_server(debug=True)

