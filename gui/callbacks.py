# Third Party Imports
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Local Imports
from gui.app import app
from db.db import DB


# Set app interval

# @app.callback(Output('app-interval', 'interval'),
#                 [Input('settings-local-store', 'data')])
# def get_app_interval(data):
#     if data is None:
#         raise PreventUpdate
#     return data['refresh_slide']*1000


# # Data Input

# @app.callback(Output('settings-local-store', 'data'),
#                 [Input('refresh-slider', 'value')])
# def update_app_interval(value):
#     if value is None:
#         raise PreventUpdate
#     return {'refresh_slide': value}


# # Data Loading

# @app.callback(Output('refresh-slider', 'value'),
#                 [Input('nav-bar', 'value')],
#                 [State('settings-local-store', 'data')])
# def load_settings_data(value, data):
#     # print(data)
#     if value == 'settings':
#         return data['refresh_slide']


# # Securities

# @app.callback(Output('local-security-modal', 'is_open'),
#                 [Input('local-security-modal-button', 'n_clicks')],
#                 [State('local-security-modal', 'is_open')])
# def open_local_security_modal(n_clicks, is_open):
#     if n_clicks:
#         return not is_open
#     return is_open

# @app.callback(Output('local-security-dropdown', 'value'),
#                 [Input('local-security-button', 'n_clicks')],
#                 [State('local-security-dropdown', 'value'),
#                 State('local-security-slider', 'value')])
# def save_security(n_clicks, dropdown_value, slider_value):
#     if n_clicks:
#         # server.save_security_local(symbols=dropdown_value, period=slider_value)
#         return None

@app.callback(Output('blank', 'children'),
                [Input('save-ingredient', 'n_clicks')],
                [State('ingredient-name', 'value'), State('ingredient-category', 'value'), State('ingredient-serving-quantity', 'value'),
                State('ingredient-serving-unit', 'value'), State('ingredient-protein', 'value'), State('ingredient-fat', 'value'),
                State('ingredient-carbohydrate', 'value'), State('ingredient-fiber', 'value'), State('ingredient-sugar', 'value')])
def ingredient_to_db_callback(clicks, name, category, serving_quantity, serving_unit, protein, fat, carbs, fiber, sugar):
    if clicks is not None:
        ingredient = {'name': name, 'category': category, 'serving_quantity': serving_quantity,
                    'serving_unit': serving_unit, 'protein': protein, 'fat': fat,
                    'carbs': carbs, 'fiber': fiber, 'sugar': sugar}
        db = DB() 
        db.ingredient_to_db(ingredient)
        return None

@app.callback([
    Output('ingredient-name','value'),
    Output('ingredient-category','value'),
    Output('ingredient-serving-quantity','value'),
    Output('ingredient-serving-unit','value'),
    Output('ingredient-protein','value'),
    Output('ingredient-fat','value'),
    Output('ingredient-carbohydrate','value'),
    Output('ingredient-fiber','value'),
    Output('ingredient-sugar','value'),
], [Input('ingredient-list-dropdown','value')])
def db_to_ingredient_callback(value):
    if value is not None:
        db = DB() 
        ingredient = db.query_name('ingredients',value)
        name = ingredient['name']
        category = ingredient['category']
        serving_quantity = ingredient['serving_quantity']
        serving_unit = ingredient['serving_unit']
        protein = ingredient['protein']
        fat = ingredient['fat']
        carbs = ingredient['carbs']
        fiber = ingredient['fiber']
        sugar = ingredient['sugar']
        return name,category,serving_quantity,serving_unit,protein,fat,carbs,fiber,sugar
    else:
        return '','','','','','','','',''