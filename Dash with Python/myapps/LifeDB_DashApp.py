import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://admin:adminrocks@db01.i7iwq.gcp.mongodb.net/lifeworks?retryWrites=true&w=majority")
db = cluster["lifeworks"]
collection = db["diary"]

ls = list(collection.find({}))

months_set = set([])

for i in ls:
    months_set.add(i['_id'][0:3]+' '+i['_id'][-4:])

months = list(months_set)

def stats(activity):
    data = {}

    for m in months:
        c = 0
        for i in ls:
            if i['_id'][0:3]+' '+i['_id'][-4:] == m and i[activity] == True:
                c += 1
        data[m] = c

    return data

#-------------Extracting Data------------------------------------

exercise_data = stats("excercise")

meditation_data = stats("meditation")

books_data = stats("book")

#-------------Data------------------------------------

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig1 = go.Figure(data=[
    go.Bar(name='Exercise', x=[x for x in exercise_data.keys()], y=[x for x in exercise_data.values()]),
    go.Bar(name='Meditation', x=[x for x in meditation_data.keys()], y=[x for x in meditation_data.values()]),
    go.Bar(name='Book Reading', x=[x for x in books_data.keys()], y=[x for x in books_data.values()]),
])

fig1.update_layout(
    width=700,
    height=600,
)

app.layout = html.Div(children=[

    html.H1(
        children = "LifeDB Exercise Statistics",
        style = {
            'textAlign' : 'center'
        }
    ),

    dcc.Graph(
        id = "stats-graph",
        figure=fig1
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)




