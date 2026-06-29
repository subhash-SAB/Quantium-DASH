from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
from style import layout

app=Dash(__name__)
app.layout=layout

df=pd.read_csv('S:/QUANTIUM/final_ouput.csv')
df['date']=pd.to_datetime(df['date'])
df=df.sort_values('date')
fig=px.line(
   df,
   x='date',
   y='sales',
   title='pink morsel weekly sales',
   labels={'date':'Date', 'sales': 'Sales ($)'},
   color_discrete_sequence=["#1EE947"],
)

fig.add_vline(
   x=pd.Timestamp("2021-01-15"),
   line_dash="dash",
   line_color="#555",
   annotation_text="Price increase(15 jan 2021)",
   annotation_position="top left",

)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(region):

    if region == "all":
        filtered = df
    else:
        filtered = df[df["region"].str.lower() == region]

    fig = px.line(
        filtered,
        x="date",
        y="sales",
        title="Pink Morsel Weekly Sales",
        labels={"date": "Date", "sales": "Sales ($)"},
        color_discrete_sequence=["#19EC4D"]
    )

    fig.add_vline(
        x=pd.Timestamp("2021-01-15"),
        line_dash="dash",
        line_color="#555",
        annotation_text="Price increase (15 Jan 2021)",
        annotation_position="top left"
    )

    return fig



if __name__ == "__main__":
    app.run(debug=True)
