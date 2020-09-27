import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'India' : ['Lucknow', 'Ajmer', 'Pappuganj'],
    'UK' : ['Scotland', 'Wales', 'Ireland']
}

app.layout = html.Div([
    dcc.RadioItems(
        id = 'countries-radio',
        options = [{'label' : k, 'value' : k} for k in all_options.keys()],
        value = 'India'
    ),

    html.Hr(),

    dcc.RadioItems(id='cities-radio'),

    html.Hr(),

    html.Div(id = 'display-selected-values')
])

#-------------------------------------------------------------------------------------------------------
#The first callback updates the available options in the second RadioItems component based off of the selected value in the first RadioItems component
@app.callback(
    Output('cities-radio', 'options'),
    [Input('countries-radio', 'value')]
)

def set_cities_options(selected_country):
    return [{'label' : i, 'value' : i} for i in all_options[selected_country]]

#-------------------------------------------------------------------------------------------------------
#The second callback sets an initial value when the options property changes: it sets it to the first value in that options array.
@app.callback(
    Output('cities-radio','value'),
    [Input('cities-radio', 'options')]
)

def set_cities_value(available_options):
    return available_options[0]['value']

#-------------------------------------------------------------------------------------------------------
# The final callback displays the selected value of each component
@app.callback(
    Output('display-selected-values', 'children'),
    [Input('countries-radio', 'value'),
    Input('cities-radio', 'value')]
)

def set_display_children(selected_country, selected_city):
    return f"{selected_city} is a city in {selected_country}"

#-------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run_server(debug=True)

