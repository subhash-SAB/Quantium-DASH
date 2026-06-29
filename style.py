from dash import html, dcc

layout = html.Div(
    [
        html.H1(
            "Soul Foods - Pink Morsels Sales Visualizer",
            style={"textAlign": "center", "color": "#0B1389"}
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={
                "textAlign": "center",
                "marginBottom": "20px"
            }
        ),

        dcc.Graph(id="sales-chart")
    ],
    style={
        "backgroundColor": "#DEB3D5",
        "padding": "30px",
        "fontFamily": "Arial"
    }
)
