import plotly_express as px
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv('data.csv')

fig=ff.create_distplot([df["AvgRating"].tolist()],["AvgRating"])
fig.show()