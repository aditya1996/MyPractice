import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in text box to see callbacks in action!!"),
    html.Div([
        "Input :",
        dcc.Input(id="my-input", value="2", type="text"),
    ]),
    html.Br(),
    html.Div(id="my-output"),
])

@app.callback(
    Output(component_id="my-output", component_property="children"),
    [Input(component_id="my-input", component_property="value")]
)

def update_div(input_value):
    try:
        r = int(input_value)*2
        return f"Output : {r}"
    except:
        return "Give a valid number!!"

if __name__ == "__main__":
    app.run_server(debug=True)

