from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app

list_of_lacations = {
    "All": 0,
    "Manhattan": 1,
    "Bronx": 2,
    "Brooklyn": 3,
    "Queens": 4,
    "State Island": 5
}

slider_size = [100, 500, 1000, 10000, 10000000]


controles = dbc.Row([

    html.Img(id='logo', src=app.get_asset_url(
        'python.jpeg'), style={'width': '50%'}),
    html.H3('Vendas de imóveis - NYC', style={'margin-top': '30px'}),
    html.P('Utilize este dashboard para analisar as vendas em New York no período 1 ano.'),

    html.H4('Distrito', style={'margin-top': '50px', 'margin-botton': '25px'}),

    dcc.Dropdown(
        id='location-drop',
        options=[{'label': i, 'value': j}
                 for i, j in list_of_lacations.items()],
        value=0,
        placeholder='Selecione um distrito'
    ),

    html.H4('Metragem m²', style={
            'margin-top': '20px', 'margin-bottom': '20px'}),

    dcc.Slider(
        min=0, max=4, id='slider',
        marks={i: str(j) for i, j in enumerate(slider_size)}
    ),
    html.H4('Variável de controle', style={
            'margin-top': '50px', 'margin-botton': '25px'}),

    dcc.Dropdown(
        id='drop-color',
        options=[{'label': 'YEAR BUILT', 'value': 'YEAR BUILT'},
                 {'label': 'TOTAL UNITS', 'value': 'TOTAL UNITS'},
                 {'label': 'SALE PRICE', 'value': 'SALE PRICE'}],
        value='SALE PRICE',

    ),

])
