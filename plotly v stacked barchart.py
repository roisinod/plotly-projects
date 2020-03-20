# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
# create a DataFrame from the .csv file:
df = pd.read_csv('mocksurvey.txt', index_col=0)
print(df.head())
print(df.columns)
# create traces using a list comprehension:


data = [go.Bar(
    y = df[response],
    x = df.index,
    name=response)
    for response in df.columns]
# create a layout, remember to set the barmode here
layout = go.Layout(
    title='Survey Results',
barmode='stack'
)


# create a fig from data & layout, and plot the fig.
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='bar5.html')