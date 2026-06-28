from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px


df=pd.read_csv('S:/QUANTIUM/final_ouput.csv')
df['date']=pd.to_datetime(df['date'])
df=df.sort_values('date')
fig=px.line(
   df,
   x='date',
   y='sales',
   title='pink morsel weekly sales',
   labels={'date':'Date', 'sales': 'Sales ($)'},
   color_discrete_sequence=["#E91E8C"],
)

fig.add_vline(
   x=pd.Timestamp("2021-01-15"),
   line_dash="dash",
   line_color="#555",
   annotation_text="Price increase(15 jan 2021)",
   annotation_position="top left",

)

app=Dash(__name__)
app.layout=html.Div([
   html.H1("Soul Foods-pink morsel sales visualizer"),
   dcc.Graph(id="sales-chart", figure=fig),
])

if __name__ == "__main__":
   app.run(debug=True)
