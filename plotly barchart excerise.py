#######
# Objective: Create a bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('mocksurvey.txt')
print(df.head())
print(df.columns)
# create traces using a list comprehension:
trace1 = go.Bar(
    x=df['Unnamed: 0'],
    y=df['Strongly Agree'],
    name = 'Strongly Agree',
    marker=dict(color='Gold'))

trace2 = go.Bar(
    x=df['Unnamed: 0'],
    y=df['Somewhat Agree'],
    name='Somewhat Agree',
    marker=dict(color='Grey')
)

trace3 = go.Bar(
    x=df['Unnamed: 0'],
    y=df['Neutral'],
    name='Neutral',
    marker=dict(color='Greenyellow')
)
trace4 = go.Bar(
    x=df['Unnamed: 0'],
    y=df['Somewhat Disagree'],
    name='Somewhat Disagree',
    marker=dict(color='Hotpink')
)
trace5 = go.Bar(
    x=df['Unnamed: 0'],
    y=df['Strongly Disagree'],
    name='Strongly Disagree',
    marker=dict(color='Aquamarine')
)



# create a layout, remember to set the barmode here

data = [trace1, trace2, trace3, trace4, trace5]
layout = go.Layout(
    title='Survey Results'
)



# create a fig from data & layout, and plot the fig.
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar2.html')
