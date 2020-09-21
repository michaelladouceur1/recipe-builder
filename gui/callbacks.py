# Third Party Imports
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import json

# Local Imports
from gui.app import app
from db.db import DB


# ADD-INGREDIENT-TO-DB-CALLBACK

@app.callback(Output('blank', 'children'),
                [Input('save-ingredient', 'n_clicks'),
                Input('edit-ingredient', 'n_clicks')],
                [State('ingredient-name', 'value'), 
                State('ingredient-category', 'value'), 
                State('ingredient-serving-gram', 'value'),
                State('ingredient-serving-tbsp', 'value'),
                State('ingredient-serving-oz', 'value'),
                State('ingredient-serving-lbs', 'value'),
                State('ingredient-serving-piece', 'value'),
                State('ingredient-serving-ml', 'value'),
                State('ingredient-serving-cup', 'value'),
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
def add_ingredient_to_db_callback(save_clicks,
                                edit_clicks,
                                name, 
                                category, 
                                serving_gram,
                                serving_tbsp,
                                serving_oz,
                                serving_lbs,
                                serving_piece,
                                serving_ml,
                                serving_cup,
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
    
    ingredient = {'name': name, 
                    'category': category, 
                    'serving_gram': serving_gram,
                    'serving_tbsp': serving_tbsp,
                    'serving_oz': serving_oz,
                    'serving_lbs': serving_lbs,
                    'serving_piece': serving_piece,
                    'serving_ml': serving_ml,
                    'serving_cup': serving_cup,
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
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'save-ingredient' in changed_id:
        db = DB() 
        db.add_ingredient_to_db(ingredient,'save')
        return None
    elif 'edit-ingredient' in changed_id:
        db = DB()
        db.add_ingredient_to_db(ingredient,'edit')
        return None
    else:
        print('No buttons pressed')


# DB-TO-INGREDIENT-CALLBACK

@app.callback([
    Output('ingredient-name','value'),
    Output('ingredient-category','value'),
    Output('ingredient-serving-gram','value'),
    Output('ingredient-serving-tbsp', 'value'),
    Output('ingredient-serving-oz', 'value'),
    Output('ingredient-serving-lbs', 'value'),
    Output('ingredient-serving-piece', 'value'),
    Output('ingredient-serving-ml', 'value'),
    Output('ingredient-serving-cup', 'value'),
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
        ingredient = db.query_by_one_param('ingredients','name',value)[0]
        name = ingredient['name']
        category = ingredient['category']
        serving_gram = ingredient['serving_gram']
        serving_tbsp = ingredient['serving_tbsp']
        serving_oz = ingredient['serving_oz']
        serving_lbs = ingredient['serving_lbs']
        serving_piece = ingredient['serving_piece']
        serving_ml = ingredient['serving_ml']
        serving_cup = ingredient['serving_cup']
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
        return name,category,serving_gram,serving_tbsp,serving_oz,\
                serving_lbs,serving_piece,serving_ml,serving_cup,\
                brand,store,calories,protein,fat,carbs,fiber,sugar,\
                sat,mono,poly,omega3,omega6,vitamin_a,vitamin_c,\
                vitamin_d,vitamin_e,vitamin_k,thiamin,\
                riboflavin,niacin,vitamin_b6,folate,\
                vitamin_b12,pantothenic_acid,calcium,\
                iron,magnesium,phosphorus,potassium ,zinc
    else:
        return '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''


# RECIPE-INGREDIENT-OPTIONS-CALLBACK

@app.callback(Output('recipe-ingredient','options'),
                [Input('recipe-ingredient-category','value')])
def recipe_ingredient_options(value):
    if value is not None:
        db = DB()
        names = db.return_by_one_param('ingredients','category',value)
        return [{'label': i, 'value': i} for i in names]
    else:
        db = DB()
        names = db.return_all_names('ingredients')
        return [{'label': i, 'value': i} for i in names]


# RECIPE-INGREDIENT-UNIT-OPTIONS-CALLBACK

@app.callback(Output('recipe-ingredient-unit','options'),
                [Input('recipe-ingredient','value')])
def recipe_ingredient_unit_options(value):
    if value is not None:
        db = DB()
        units = db.return_ingredient_units('ingredients','name',value)
        return [{'label': i, 'value': i} for i in units]
    else:
        return [{'label': '', 'value': ''}]


# ADD-INGREDIENT-TO-RECIPE-CALLBACK

@app.callback(Output('recipe-ingredients-table','data'),
                [Input('add-ingredient-to-recipe','n_clicks')],
                [State('recipe-ingredients-table','data'),
                State('recipe-ingredient','value'),
                State('recipe-ingredient-quantity','value'),
                State('recipe-ingredient-unit','value')])
def add_ingredient_to_recipe(n_clicks,rows,name,quantity,unit):
    if n_clicks > 0 and n_clicks is not None:
        db = DB()
        ingredient = db.query_by_one_param('ingredients','name',name)[0]
        for i in ingredient.keys():
            if i.find(unit) != -1:
                db_quantity = float(ingredient[i])
        rows.append({
            'ingredient': name,
            'quantity': quantity,
            'unit': unit,
            'calories': round(((float(quantity)/db_quantity)*float(ingredient['calories'])),2),
            'protein': round(((float(quantity)/db_quantity)*float(ingredient['protein'])),2),
            'fat': round(((float(quantity)/db_quantity)*float(ingredient['fat'])),2),
            'carbs': round(((float(quantity)/db_quantity)*float(ingredient['carbs'])),2),
        })
    return rows

@app.callback([Output('recipe-total-calories','children'),
                Output('recipe-serving-calories','children'),
                Output('recipe-total-protein','children'),
                Output('recipe-serving-protein','children'),
                Output('recipe-total-fat','children'),
                Output('recipe-serving-fat','children'),
                Output('recipe-total-carbs','children'),
                Output('recipe-serving-carbs','children')],
                [Input('recipe-ingredients-table','data'),
                Input('recipe-servings-slider','value')],
                [State('recipe-ingredients-table','data'),
                State('recipe-servings-slider','value')])
def recipe_data_sum(input_data,input_servings,state_data,servings):
    data = {
        'total-calories': 0,
        'serving-calories': 0,
        'total-protein': 0,
        'serving-protein': 0,
        'total-fat': 0,
        'serving-fat': 0,
        'total-carbs': 0,
        'serving-carbs': 0
    }
    if input_data is not None or input_servings is not None:
        for i in state_data:
            data['total-calories'] += i['calories']
            data['total-protein'] += i['protein']
            data['total-fat'] += i['fat']
            data['total-carbs'] += i['carbs']
    data['serving-calories'] = data['total-calories']/servings
    data['serving-protein'] = data['total-protein']/servings
    data['serving-fat'] = data['total-fat']/servings
    data['serving-carbs'] = data['total-carbs']/servings

    return round(data['total-calories'],1),round(data['serving-calories'],1),\
            round(data['total-protein'],1),round(data['serving-protein'],1),\
            round(data['total-fat'],1),round(data['serving-fat'],1),\
            round(data['total-carbs'],1),round(data['serving-carbs'],1)

# @app.callback(Output('blank', 'children'),
#                 [Input('delete-ingredient','n_clicks')],
#                 [State('ingredient-name','value')])
# def delete_ingredient(n1,name):
#     changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
#     if 'delete-ingredient' in changed_id:
#         print(f'Deleting ingredient {name}')
#         db = DB()
#         db.delete(name)
#         return None


# SERVING-MODAL-CALLBACK

@app.callback(Output('serving-modal','is_open'),
                [Input('open-serving-modal','n_clicks'),
                Input('close-serving-modal','n_clicks')],
                [State('serving-modal','is_open')])
def serving_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# FAT-MODAL-CALLBACK

@app.callback(Output('fat-modal','is_open'),
                [Input('open-fat-modal','n_clicks'),
                Input('close-fat-modal','n_clicks')],
                [State('fat-modal','is_open')])
def fat_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open