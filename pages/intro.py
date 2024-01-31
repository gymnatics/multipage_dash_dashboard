import dash
from dash import html
import navigation
dash.register_page(__name__, path='/home', name="Introduction 😃")

####################### PAGE LAYOUT #############################
layout = html.Div(
    children =[
    navigation.navbar,
    html.Div(children=[
    html.Div(children=[
        html.H2("Robot System Dashboard"),
        html.Iframe(src="http://127.0.0.1:8055/", style={"width":"100%"})
    ])
], className="bg-light p-4 m-2")])