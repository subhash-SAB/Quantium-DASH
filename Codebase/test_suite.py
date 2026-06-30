import pytest
from app_plot import app

def test_header_present():
    header = app.layout.children[0]
    assert header.children == "Soul Foods - Pink Morsels Sales Visualizer"

def test_graph_present():
    graph = app.layout.children[2]
    assert graph.id == "sales-chart"

def test_region_picker_present():
    radio = app.layout.children[1]

    assert radio.id == "region-filter"

    values = [item["value"] for item in radio.options]

    assert values == [
        "all",
        "north",
        "east",
        "south",
        "west"
    ]

   