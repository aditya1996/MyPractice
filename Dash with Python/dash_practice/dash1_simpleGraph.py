import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame({
    'Fruit' : ["Apples","Mangoes","Bananas","Apples","Mangoes","Bananas"],
    'Amount' : [4,1,2,3,4,6],
    "City" : ["Lucknow","Ajmer","Lucknow","Ajmer","Lucknow","Ajmer"]
})

fig = px.bar(df, x = "Fruit",y = "Amount", color = "City", barmode="group") # Making a Plotly Figure

app.layout = html.Div(children=[
    html.H1(
        children="Hello Dash",
        style={
            'textAlign' : 'center'
        }
        ),

    html.Div(
        children=['''
        Dash. A Web Application framework for python
    '''],
        style={
            'textAlign' : 'center'
        }
    ),

    dcc.Graph(
        id = 'example-graph',
        figure=fig
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)