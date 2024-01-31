from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash
import plotly.express as px

px.defaults.template = "ggplot2"

external_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" ]

app = Dash(__name__, pages_folder='pages', use_pages=True, external_stylesheets= [dbc.themes.FLATLY], suppress_callback_exceptions=True)


if __name__ == '__main__':
	app.run(debug=True)