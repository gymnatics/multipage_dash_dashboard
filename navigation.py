import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="home")),
        dbc.NavItem(dbc.NavLink("Robot Controls", href="dataset")),
        dbc.NavItem(dbc.NavLink("Staff Management", href="distribution")),
    ],
    brand="Workflow Management App",
    brand_style={"text_align":"left"},
    brand_href="home",
    color="primary",
    dark=True,
)