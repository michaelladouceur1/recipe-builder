# Third Party Imports
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Local Imports
from gui.app import app
from db.db import DB

# navigation

navigation = html.Div(id='navbar',children=[
    
])

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Click here", color="success"),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.H2("Recipes", className="card-text", style={'align-content': 'center'})
                    ),
                    dbc.Col(
                        dbc.Button('Save Recipe', color='primary', id='save-recipe')
                    )
                ], className='page-header'
            ),
            dbc.Row(
                [
                    # LEFT COLUMN
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardImg(src=app.get_asset_url("placeholder.png"), top=True, id='recipe-image'),
                                dbc.CardBody(
                                    [
                                        html.H4("Card title", className="card-title"),
                                        html.P(
                                            "Some quick example text to build on the card title and "
                                            "make up the bulk of the card's content.",
                                            className="card-text",
                                        ),
                                        dbc.Button("Go somewhere", color="primary"),
                                    ]
                                ),
                            ]
                        ), width=3
                    ),

                    # RIGHT COLUMN
                    dbc.Col(children=[
                        # ROW 1
                        dbc.Row(
                            [
                                dbc.Col([
                                    dbc.Label('Recipe Name', className='label'),
                                    dbc.Input(id='recipe-name', placeholder='Name...')
                                ], className='ingredient-element'
                                ),
                                dbc.Col([
                                    dbc.Label('Recipe Category', className='label'),
                                    dcc.Dropdown(
                                        id='recipe-category',
                                        options=[
                                            {'label': 'Meat', 'value': 'Meat'},
                                            {'label': 'Vegetable', 'value': 'Vegetable'},
                                            {'label': 'Fruit', 'value': 'Fruit'},
                                            {'label': 'Grain', 'value': 'Grain'},
                                            {'label': 'Fat/Oil', 'value': 'Fat/Oil'},
                                            {'label': 'Miscellaneous', 'value': 'Miscellaneous'}
                                        ],
                                        value='Meat'
                                    )
                                ], className='ingredient-element'
                                ),
                                dbc.Col([
                                    dbc.Label('Serving Quantity', className='label'),
                                    dbc.Input(id='recipe-serving-quantity', type='number', placeholder='Serving quantity...')
                                ], className='ingredient-element'
                                ),
                                dbc.Col([
                                    dbc.Label('Serving Unit', className='label'),
                                    dcc.Dropdown(
                                        id='recipe-serving-unit',
                                        options=[
                                            {'label': 'Gram', 'value': 'Gram'},
                                            {'label': 'Tbsp', 'value': 'Tbsp'},
                                            {'label': 'Ounce', 'value': 'Ounce'},
                                            {'label': 'Pound', 'value': 'Pound'},
                                            {'label': 'Piece', 'value': 'Piece'},
                                            {'label': 'MilliLiter', 'value': 'MilliLiter'}
                                        ],
                                        value='Gram'
                                    )
                                ], className='ingredient-element'
                                )
                            ]
                        ),

                        # ROW 2
                        dbc.Row(
                            [
                                dbc.Col([
                                    dbc.Label('Protein Content', className='label'),
                                    dbc.Input(id='recipe-protein', type='number', placeholder='Protein...')
                                ], className='ingredient-element'
                                ),
                                dbc.Col([
                                    dbc.Label('Fat Content', className='label'),
                                    dbc.Input(id='recipe-fat', type='number', placeholder='Fat...')
                                ], className='ingredient-element'
                                ),
                                dbc.Col([
                                    dbc.Label('Carbohydrate Content', className='label'),
                                    dbc.Input(id='recipe-carbohydrate', type='number', placeholder='Carbohydrate...')
                                ], className='ingredient-element'
                                )
                            ]
                        ),

                        # ROW 3
                        dbc.Row(
                            [
                                dbc.Col([
                                    dbc.Label('Fiber Content', className='label'),
                                    dbc.Input(id='recipe-fiber', type='number', placeholder='Fiber...')
                                ], className='ingredient-element'
                                ),
                                dbc.Col([
                                    dbc.Label('Sugar Content', className='label'),
                                    dbc.Input(id='recipe-sugar', type='number', placeholder='Sugar...')
                                ], className='ingredient-element'
                                ),
                            ]
                        ),
                    ])
                ]
            ),
        ]
    ),
    className="mt-3",
)

db = DB()
ingredients = db.return_all_names('ingredients')
ingredients_options = []
for i in ingredients:
    ingredients_options.append({'label': i, 'value': i})

tab3_content = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.H2('Ingredients')
                    ),
                ], className='page-header'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Button('Save Ingredient', color='primary', id='save-ingredient')
                    ),
                    dbc.Col(
                        dcc.Dropdown(id='ingredient-list-dropdown', options=ingredients_options)
                    )
                ], className='page-control-menu'
            ),
            dbc.Row(
                [
                    dbc.Col(children=[
                        # ROW 1
                        dbc.Row(
                            [
                                dbc.Col([
                                    dbc.Label('Ingredient Name', className='label'),
                                    dbc.Input(id='ingredient-name', placeholder='Name...')
                                ], className='ingredient-element'
                                ),
                                dbc.Col([
                                    dbc.Label('Ingredient Category', className='label'),
                                    dcc.Dropdown(
                                        id='ingredient-category',
                                        options=[
                                            {'label': 'Meat', 'value': 'Meat'},
                                            {'label': 'Vegetable', 'value': 'Vegetable'},
                                            {'label': 'Fruit', 'value': 'Fruit'},
                                            {'label': 'Grain', 'value': 'Grain'},
                                            {'label': 'Fat/Oil', 'value': 'Fat/Oil'},
                                            {'label': 'Miscellaneous', 'value': 'Miscellaneous'}
                                        ],
                                        value='Meat'
                                    )
                                ], className='ingredient-element'
                                ),
                                dbc.Col([
                                    dbc.Label('Serving Quantity', className='label'),
                                    dbc.Input(id='ingredient-serving-quantity', type='number', placeholder='Serving quantity...')
                                ], className='ingredient-element'
                                ),
                                dbc.Col([
                                    dbc.Label('Serving Unit', className='label'),
                                    dcc.Dropdown(
                                        id='ingredient-serving-unit',
                                        options=[
                                            {'label': 'Gram', 'value': 'Gram'},
                                            {'label': 'Tbsp', 'value': 'Tbsp'},
                                            {'label': 'Ounce', 'value': 'Ounce'},
                                            {'label': 'Pound', 'value': 'Pound'},
                                            {'label': 'Piece', 'value': 'Piece'},
                                            {'label': 'MilliLiter', 'value': 'MilliLiter'}
                                        ],
                                        value='Gram'
                                    )
                                ], className='ingredient-element'
                                )
                            ]
                        ),

                        # ROW 2
                        dbc.Row(
                            [
                                dbc.Col([
                                    dbc.Label('Protein Content', className='label'),
                                    dbc.Input(id='ingredient-protein', type='number', placeholder='Protein...')
                                ], className='ingredient-element'
                                ),
                                dbc.Col([
                                    dbc.Label('Fat Content', className='label'),
                                    dbc.Input(id='ingredient-fat', type='number', placeholder='Fat...')
                                ], className='ingredient-element'
                                ),
                                dbc.Col([
                                    dbc.Label('Carbohydrate Content', className='label'),
                                    dbc.Input(id='ingredient-carbohydrate', type='number', placeholder='Carbohydrate...')
                                ], className='ingredient-element'
                                )
                            ]
                        ),

                        # ROW 3
                        dbc.Row(
                            [
                                dbc.Col([
                                    dbc.Label('Fiber Content', className='label'),
                                    dbc.Input(id='ingredient-fiber', type='number', placeholder='Fiber...')
                                ], className='ingredient-element'
                                ),
                                dbc.Col([
                                    dbc.Label('Sugar Content', className='label'),
                                    dbc.Input(id='ingredient-sugar', type='number', placeholder='Sugar...')
                                ], className='ingredient-element'
                                ),
                            ]
                        ),
                    ])
                ],
                className='main-row'
            ),

            # BLANK
            dbc.Row(
                [
                    html.P()
                ], id='blank'
            )
        ]
    ),
    className="mt-3",
    id='ingredient-menu'
)


tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Planner", className='tabs'),
        dbc.Tab(tab2_content, label="Recipes", className='tabs'),
        dbc.Tab(tab3_content, label="Ingredients", className='tabs'),
    ], id='tabs-container'
)