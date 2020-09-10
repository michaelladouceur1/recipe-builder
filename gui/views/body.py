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
    className="mt-3 menu-page",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.H2("RECIPES", className="card-text", style={'align-content': 'center'})
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
                                dbc.CardHeader([
                                    dbc.Row(children=[
                                        dbc.Col(
                                        dcc.Dropdown(
                                        id='recipe-list-category-dropdown',
                                        options=[
                                            {'label': 'All', 'value': 'Meat'},
                                            {'label': 'Breakfast', 'value': 'Vegetable'},
                                            {'label': 'Lunch/Dinner', 'value': 'Fruit'},
                                            {'label': 'Snack', 'value': 'Grain'},
                                            {'label': 'Dessert', 'value': 'Fat/Oil'},
                                            {'label': 'Miscellaneous', 'value': 'Miscellaneous'}
                                        ],
                                        placeholder='Category...'
                                    ),width=4
                                    ),
                                    dbc.Col(
                                        dcc.Dropdown(
                                        id='recipe-list-dropdown',
                                        options=[
                                            {'label': 'Meat', 'value': 'Meat'},
                                            {'label': 'Vegetable', 'value': 'Vegetable'},
                                            {'label': 'Fruit', 'value': 'Fruit'},
                                            {'label': 'Grain', 'value': 'Grain'},
                                            {'label': 'Fat/Oil', 'value': 'Fat/Oil'},
                                            {'label': 'Miscellaneous', 'value': 'Miscellaneous'}
                                        ],
                                        placeholder='Search Recipe...'
                                    )
                                    )
                                    ],no_gutters=True)
                                ],id='recipe-list-container'),
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
    className="mt-3 menu-page",
)

db = DB()
ingredients = db.return_all_names('ingredients')
ingredients_options = []
for i in ingredients:
    ingredients_options.append({'label': i, 'value': i})

tab3_content = dbc.Card(
    dbc.CardBody(
        [
            # NAV ROW
            dbc.Row(
                [
                    dbc.Col(
                        html.H2('INGREDIENTS'),
                        width=3
                    ),
                    dbc.Col(
                        dbc.ButtonGroup([
                            dbc.Button(html.I(className='far fa-save'), color='secondary', id='save-ingredient'),
                            dbc.Button(html.I(className='fas fa-edit'), color='secondary', id='edit-ingredient'),
                            dbc.Button(html.I(className='fas fa-backspace'), color='secondary', id='clear-ingredient')
                        ]), width=2
                    ),
                    dbc.Col(),
                    dbc.Col(
                        dcc.Dropdown(id='ingredient-list-dropdown',placeholder='Search Ingredients...', options=ingredients_options),
                        width=3
                    )
                ], className='page-header'
            ),

            # MAIN MENU ROW
            dbc.Row(
                [
                    # BASIC DETAILS COLUMN
                    dbc.Col(children=[
                        dbc.Card(children=[
                            dbc.CardHeader('Basic Details'),
                            dbc.CardBody(children=[
                                dbc.Label('Ingredient Name', className='label'),
                                dbc.Input(id='ingredient-name', placeholder='Name...'),
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
                                ),
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Label('Serving Quantity', className='label'),
                                        dbc.Input(id='ingredient-serving-quantity', type='number', placeholder='Serving quantity...')
                                    ]),
                                    dbc.Col([
                                        dbc.Label('Serving Unit', className='label'),
                                        dcc.Dropdown(
                                            id='ingredient-serving-unit',
                                            options=[
                                                {'label': 'Gram', 'value': 'Gram'},
                                                {'label': 'Tbsp.', 'value': 'Tbsp.'},
                                                {'label': 'Oz.', 'value': 'Oz.'},
                                                {'label': 'Lbs.', 'value': 'Lbs.'},
                                                {'label': 'Piece', 'value': 'Piece'},
                                                {'label': 'mL', 'value': 'mL'},
                                                {'label': 'cup', 'value': 'cup'}
                                            ],
                                            value='Gram'
                                        )
                                    ])
                                ]),
                                dbc.Label('Preferred Brand', className='label'),
                                dbc.Input(id='preferred-brand', placeholder='Brand...'),
                                dbc.Label('Suggested Store', className='label'),
                                dcc.Dropdown(
                                    id='suggested-store',
                                    options=[
                                        {'label': 'Aldi', 'value': 'Aldi'},
                                        {'label': 'Fresh Thyme', 'value': 'Fresh Thyme'},
                                        {'label': 'Natures Best', 'value': 'Natures Best'},
                                        {'label': 'Marianos', 'value': 'Marianos'},
                                        {'label': 'H-Mart', 'value': 'H-Mart'},
                                        {'label': 'Whole Foods', 'value': 'Whole Foods'}
                                    ],
                                    value='',
                                    multi=True
                                )
                            ])
                        ])
                    ], className='main-card'),

                    # MACRO DETAILS COLUMN
                    dbc.Col(children=[
                        dbc.Card(children=[
                            dbc.CardHeader('Macronutrient Details'),
                            dbc.CardBody(children=[
                                dbc.Label('Calories', className='label'),
                                dbc.Input(id='ingredient-calories', type='number', placeholder='Calories...'),
                                dbc.Label('Protein Content (g)', className='label'),
                                dbc.Input(id='ingredient-protein', type='number', placeholder='Protein...'),
                                dbc.Label('Fat Content (g)', className='label'),
                                dbc.Row(children=[
                                    dbc.Col([
                                        dbc.Input(id='ingredient-fat', type='number', placeholder='Fat...')
                                    ]),
                                    dbc.Col([
                                        dbc.Button('...', id='open-fat-modal'),
                                        dbc.Modal([
                                            dbc.ModalHeader('Fat Details'),
                                            dbc.ModalBody([
                                                dbc.Label('Saturated Fat Content (g)', className='label'),
                                                dbc.Input(id='ingredient-saturated-fat', type='number', placeholder='Saturated Fat...'),
                                                dbc.Label('Monounsaturated Fat Content (g)', className='label'),
                                                dbc.Input(id='ingredient-monounsaturated-fat', type='number', placeholder='Monounsaturated Fat...'),
                                                dbc.Label('Polyunsaturated Fat Content (g)', className='label'),
                                                dbc.Input(id='ingredient-polyunsaturated-fat', type='number', placeholder='Polyunsaturated Fat...'),
                                                dbc.Label('Omega-3 Fat Content (mg)', className='label'),
                                                dbc.Input(id='ingredient-omega-3-fat', type='number', placeholder='Omega-3 Fat...'),
                                                dbc.Label('Omega-6 Fat Content (mg)', className='label'),
                                                dbc.Input(id='ingredient-omega-6-fat', type='number', placeholder='Omega-6 Fat...')
                                            ]),
                                            dbc.ModalFooter(
                                                dbc.Button("Close", id="close-fat-modal", className="ml-auto")
                                            ),
                                        ], 
                                        id='fat-modal', 
                                        className='modal-card',
                                        centered=True)
                                    ], width=3)
                                ]),
                                dbc.Label('Carbohydrate Content (g)', className='label'),
                                dbc.Input(id='ingredient-carbohydrate', type='number', placeholder='Carbohydrate...'),
                                dbc.Label('Fiber Content (g)', className='label'),
                                dbc.Input(id='ingredient-fiber', type='number', placeholder='Fiber...'),
                                dbc.Label('Sugar Content (g)', className='label'),
                                dbc.Input(id='ingredient-sugar', type='number', placeholder='Sugar...')
                            ])
                        ])
                    ], className='main-card'),

                    # VITAMIN AND MINERAL DETAILS COLUMN
                    dbc.Col(children=[
                        dbc.Card(children=[
                            dbc.CardHeader('Vitamin and Mineral Details'),
                            dbc.CardBody(children=[
                                dbc.Row([
                                    dbc.Col(children=[
                                        dbc.Label('Vitamin A (IU)', className='label'),
                                        dbc.Input(id='ingredient-vitamin-a', type='number', placeholder='Vitamin A...'),
                                        dbc.Label('Vitamin C (mg)', className='label'),
                                        dbc.Input(id='ingredient-vitamin-c', type='number', placeholder='Vitamin C...'),
                                        dbc.Label('Vitamin D (IU)', className='label'),
                                        dbc.Input(id='ingredient-vitamin-d', type='number', placeholder='Vitamin D...'),
                                        dbc.Label('Vitamin E (mg)', className='label'),
                                        dbc.Input(id='ingredient-vitamin-e', type='number', placeholder='Vitamin E...'),
                                        dbc.Label('Vitamin K (mcg)', className='label'),
                                        dbc.Input(id='ingredient-vitamin-k', type='number', placeholder='Vitamin K...'),
                                        dbc.Label('Thiamin (mg)', className='label'),
                                        dbc.Input(id='ingredient-thiamin', type='number', placeholder='Thiamin...'),
                                    ],width=4),
                                    dbc.Col(children=[
                                        dbc.Label('Riboflavin (mg)', className='label'),
                                        dbc.Input(id='ingredient-riboflavin', type='number', placeholder='Riboflavin...'),
                                        dbc.Label('Niacin (mg)', className='label'),
                                        dbc.Input(id='ingredient-niacin', type='number', placeholder='Niacin...'),
                                        dbc.Label('Vitamin B6 (mg)', className='label'),
                                        dbc.Input(id='ingredient-vitamin-b6', type='number', placeholder='Vitamin B6...'),
                                        dbc.Label('Folate (mcg)', className='label'),
                                        dbc.Input(id='ingredient-folate', type='number', placeholder='Folate...'),
                                        dbc.Label('Vitamin B12 (mcg)', className='label'),
                                        dbc.Input(id='ingredient-vitamin-b12', type='number', placeholder='Vitamin B12...'),
                                        dbc.Label('Pantothenic Acid (mg)', className='label'),
                                        dbc.Input(id='ingredient-pantothenic-acid', type='number', placeholder='Pantothenic Acid...'),
                                    ],width=4),
                                    dbc.Col(children=[
                                        dbc.Label('Calcium (mg)', className='label'),
                                        dbc.Input(id='ingredient-calcium', type='number', placeholder='Calcium...'),
                                        dbc.Label('Iron (mg)', className='label'),
                                        dbc.Input(id='ingredient-iron', type='number', placeholder='Iron...'),
                                        dbc.Label('Magnesium (mg)', className='label'),
                                        dbc.Input(id='ingredient-magnesium', type='number', placeholder='Magnesium...'),
                                        dbc.Label('Phosphorus (mg)', className='label'),
                                        dbc.Input(id='ingredient-phosphorus', type='number', placeholder='Phosphorus...'),
                                        dbc.Label('Potassium (mg)', className='label'),
                                        dbc.Input(id='ingredient-potassium', type='number', placeholder='Potassium...'),
                                        dbc.Label('Zinc (mg)', className='label'),
                                        dbc.Input(id='ingredient-zinc', type='number', placeholder='Zinc...'),
                                    ],width=4),
                                ])
                            ])
                        ])
                    ],width=4)
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
    className="mt-3 menu-page",
    id='ingredient-menu'
)


tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Planner", className='tabs'),
        dbc.Tab(tab2_content, label="Recipes", className='tabs'),
        dbc.Tab(tab3_content, label="Ingredients", className='tabs'),
    ], id='tabs-container'
)