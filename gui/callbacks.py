# Third Party Imports
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import json

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

# ingredient_to_db_callback
@app.callback(Output('blank', 'children'),
                [Input('save-ingredient', 'n_clicks')],
                [State('ingredient-name', 'value'), 
                State('ingredient-category', 'value'), 
                State('ingredient-serving-quantity', 'value'),
                State('ingredient-serving-unit', 'value'), 
                State('preferred-brand', 'value'),
                State('suggested-store', 'value'),
                State('ingredient-calories', 'value'), 
                State('ingredient-protein', 'value'), 
                State('ingredient-fat', 'value'),
                State('ingredient-carbohydrate', 'value'), 
                State('ingredient-fiber', 'value'), 
                State('ingredient-sugar', 'value'),
                State('ingredient-saturated-fat', 'value'),
                State('ingredient-monounsaturated-fat', 'value'),
                State('ingredient-polyunsaturated-fat', 'value'),
                State('ingredient-omega-3-fat', 'value'),
                State('ingredient-omega-6-fat', 'value'),
                State('ingredient-vitamin-a', 'value'),
                State('ingredient-vitamin-c', 'value'),
                State('ingredient-vitamin-d', 'value'),
                State('ingredient-vitamin-e', 'value'),
                State('ingredient-vitamin-k', 'value'),
                State('ingredient-thiamin', 'value'),
                State('ingredient-riboflavin', 'value'),
                State('ingredient-niacin', 'value'),
                State('ingredient-vitamin-b6', 'value'),
                State('ingredient-folate', 'value'),
                State('ingredient-vitamin-b12', 'value'),
                State('ingredient-pantothenic-acid', 'value'),
                State('ingredient-calcium', 'value'),
                State('ingredient-iron', 'value'),
                State('ingredient-magnesium', 'value'),
                State('ingredient-phosphorus', 'value'),
                State('ingredient-potassium', 'value'),
                State('ingredient-zinc', 'value'),])
def ingredient_to_db_callback(clicks, 
                                name, 
                                category, 
                                serving_quantity, 
                                serving_unit, 
                                brand,
                                store,
                                calories,
                                protein, 
                                fat, 
                                carbs, 
                                fiber, 
                                sugar,
                                sat,
                                mono,
                                poly,
                                omega3,
                                omega6,
                                vitamin_a,
                                vitamin_c,
                                vitamin_d,
                                vitamin_e,
                                vitamin_k,
                                thiamin,
                                riboflavin,
                                niacin,
                                vitamin_b6,
                                folate,
                                vitamin_b12,
                                pantothenic_acid,
                                calcium,
                                iron,
                                magnesium,
                                phosphorus,
                                potassium ,
                                zinc):
    if clicks is not None:
        ingredient = {'name': name, 
                        'category': category, 
                        'serving_quantity': serving_quantity,
                        'serving_unit': serving_unit, 
                        'preferred_brand': brand,
                        'suggested_store': json.dumps(store),
                        'calories': calories,
                        'protein': protein, 
                        'fat': fat,
                        'carbs': carbs, 
                        'fiber': fiber, 
                        'sugar': sugar,
                        'saturated_fat': sat,
                        'monounsaturated_fat': mono,
                        'polyunsaturated_fat': poly,
                        'omega_3_fat': omega3,
                        'omega_6_fat': omega6,
                        'vitamin_a': vitamin_a,
                        'vitamin_c': vitamin_c,
                        'vitamin_d': vitamin_d,
                        'vitamin_e': vitamin_e,
                        'vitamin_k': vitamin_k,
                        'thiamin': thiamin,
                        'riboflavin': riboflavin,
                        'niacin': niacin,
                        'vitamin_b6': vitamin_b6,
                        'folate': folate,
                        'vitamin_b12': vitamin_b12,
                        'pantothenic_acid': pantothenic_acid,
                        'calcium': calcium,
                        'iron': iron,
                        'magnesium': magnesium,
                        'phosphorus': phosphorus,
                        'potassium' : potassium,
                        'zinc': zinc}
        print(ingredient)
        db = DB() 
        db.ingredient_to_db(ingredient)
        return None

# db_to_ingredient_callback
@app.callback([
    Output('ingredient-name','value'),
    Output('ingredient-category','value'),
    Output('ingredient-serving-quantity','value'),
    Output('ingredient-serving-unit','value'),
    Output('preferred-brand', 'value'),
    Output('suggested-store', 'value'),
    Output('ingredient-calories','value'),
    Output('ingredient-protein','value'),
    Output('ingredient-fat','value'),
    Output('ingredient-carbohydrate','value'),
    Output('ingredient-fiber','value'),
    Output('ingredient-sugar','value'),
    Output('ingredient-saturated-fat', 'value'),
    Output('ingredient-monounsaturated-fat', 'value'),
    Output('ingredient-polyunsaturated-fat', 'value'),
    Output('ingredient-omega-3-fat', 'value'),
    Output('ingredient-omega-6-fat', 'value'),
    Output('ingredient-vitamin-a', 'value'),
    Output('ingredient-vitamin-c', 'value'),
    Output('ingredient-vitamin-d', 'value'),
    Output('ingredient-vitamin-e', 'value'),
    Output('ingredient-vitamin-k', 'value'),
    Output('ingredient-thiamin', 'value'),
    Output('ingredient-riboflavin', 'value'),
    Output('ingredient-niacin', 'value'),
    Output('ingredient-vitamin-b6', 'value'),
    Output('ingredient-folate', 'value'),
    Output('ingredient-vitamin-b12', 'value'),
    Output('ingredient-pantothenic-acid', 'value'),
    Output('ingredient-calcium', 'value'),
    Output('ingredient-iron', 'value'),
    Output('ingredient-magnesium', 'value'),
    Output('ingredient-phosphorus', 'value'),
    Output('ingredient-potassium', 'value'),
    Output('ingredient-zinc', 'value')
], [Input('ingredient-list-dropdown','value')])
def db_to_ingredient_callback(value):
    if value is not None:
        db = DB() 
        ingredient = db.query_by_name('ingredients',value)
        name = ingredient['name']
        category = ingredient['category']
        serving_quantity = ingredient['serving_quantity']
        serving_unit = ingredient['serving_unit']
        brand = ingredient['preferred_brand']
        store = json.loads(ingredient['suggested_store'])
        calories = ingredient['calories']
        protein = ingredient['protein']
        fat = ingredient['fat']
        carbs = ingredient['carbs']
        fiber = ingredient['fiber']
        sugar = ingredient['sugar']
        sat = ingredient['saturated_fat']
        mono = ingredient['monounsaturated_fat']
        poly = ingredient['polyunsaturated_fat']
        omega3 = ingredient['omega_3_fat']
        omega6 = ingredient['omega_6_fat']
        vitamin_a = ingredient['vitamin_a']
        vitamin_c = ingredient['vitamin_c']
        vitamin_d = ingredient['vitamin_d']
        vitamin_e = ingredient['vitamin_e']
        vitamin_k = ingredient['vitamin_k']
        vitamin_b6 = ingredient['vitamin_b6']
        vitamin_b12 = ingredient['vitamin_b12']
        thiamin = ingredient['thiamin']
        riboflavin = ingredient['riboflavin']
        niacin = ingredient['niacin']
        folate = ingredient['folate']
        pantothenic_acid = ingredient['pantothenic_acid']
        calcium = ingredient['calcium']
        iron = ingredient['iron']
        magnesium = ingredient['magnesium']
        phosphorus = ingredient['phosphorus']
        potassium = ingredient['potassium']
        zinc = ingredient['zinc']
        return name,category,serving_quantity,serving_unit,\
                brand,store,calories,protein,fat,carbs,fiber,sugar,\
                sat,mono,poly,omega3,omega6,vitamin_a,vitamin_c,\
                vitamin_d,vitamin_e,vitamin_k,thiamin,\
                riboflavin,niacin,vitamin_b6,folate,\
                vitamin_b12,pantothenic_acid,calcium,\
                iron,magnesium,phosphorus,potassium ,zinc
    else:
        return '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''

@app.callback(Output('fat-modal','is_open'),
                [Input('open-fat-modal','n_clicks'),
                Input('close-fat-modal','n_clicks')],
                [State('fat-modal','is_open')])
def fat_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open