import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("./dataset/matches.csv")
df_1 = df["city"].value_counts()[0:7].to_dict() # Top Seven Cities having most no. of matches | Matches played

cities = []
matches = []

for key, value in df_1.items():
    cities.append(key)
    matches.append(value)

dff = pd.DataFrame({
    'city' : cities,
    'matches' : matches
})

fig = px.bar(dff, x = "city", y = "matches", barmode = "group")

app.layout = html.Div(children=[

    html.H1(
        children = "IPL Statistics",
        style = {
            'textAlign' : 'center'
        }
    ),

    dcc.Graph(
        id = "city-matches",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)