
#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output

from app import app
from pages import dataset, distribution,intro

url_content_layout = html.Div(children=[
    dcc.Location(id="url",refresh=False),
    html.Div(id="output-div")
])

app.layout = url_content_layout

app.validation_layout = html.Div([
    url_content_layout,
    dataset.dataset_layout,
    distribution.distribution_layout,
    intro.intro_layout
])


@app.callback(Output(component_id="output-div",component_property="children"),Input(component_id="url",component_property="pathname"))
def update_output_div(pathname):
    if pathname == "/dataset":
        return  dataset.dataset_layout
    elif pathname == "/distribution":
        return distribution.distribution_layout
    elif pathname == "":
        return intro.intro_layout


if __name__ == "__main__":
    app.run_server(debug=True)