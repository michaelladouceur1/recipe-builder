import random
import math
import pprint

ingredients = {
    'chicken': {
        'quantity': 100,
        'units': 'grams',
        'carb': 0,
        'fat': 3.6,
        'protein': 31
    },
    'olive oil': {
        'quantity': 28,
        'units': 'grams',
        'carb': 0,
        'fat': 28,
        'protein': 0
    },
    'potatoes': {
        'quantity': 100,
        'units': 'grams',
        'carb': 17,
        'fat': 0.1,
        'protein': 2
    },
    'carrots': {
        'quantity': 100,
        'units': 'grams',
        'carb': 12.26,
        'fat': 0.31,
        'protein': 1.19
    },
    'avocado': {
        'quantity': 100,
        'units': 'grams',
        'carb': 9,
        'fat': 15,
        'protein': 2
    },
    'rice': {
        'quantity': 100,
        'units': 'grams',
        'carb': 35,
        'fat': 0.3,
        'protein': 2.7
    },
    'beef': {
        'quantity': 100,
        'units': 'grams',
        'carb': 0,
        'fat': 15,
        'protein': 26
    },
    'peas': {
        'quantity': 100,
        'units': 'grams',
        'carb': 14,
        'fat': 0.4,
        'protein': 5
    },
    'quinoa': {
        'quantity': 185,
        'units': 'grams',
        'carb': 39.4,
        'fat': 3.55,
        'protein': 8.14
    },
    'tomato': {
        'quantity': 91,
        'units': 'grams',
        'carb': 3.5,
        'fat': 0.2,
        'protein': 0.8
    },
    'tuna': {
        'quantity': 100,
        'units': 'grams',
        'carb': 0,
        'fat': 0.8,
        'protein': 25.5
    },
    'salmon': {
        'quantity': 100,
        'units': 'grams',
        'carb': 0,
        'fat': 13,
        'protein': 20
    },
    'sweet potatoes': {
        'quantity': 100,
        'units': 'grams',
        'carb': 20,
        'fat': 0.1,
        'protein': 1.6
    }

}

# PARAMETERS
recipe_count = 25
ingredient_min = 1
ingredient_max = 10
ingredient_amount_min = 25
ingredient_amount_max = 100

# PROTO: macro = [calories, meals, carbs, fat, protein]
target = [2280,3,40,200,80]

recipes = []

def create_recipes():
	for i in range(recipe_count):
		ingredient_count = random.randint(ingredient_min,ingredient_max)
		for j in range(ingredient_count):
			ingredient = random.choice(list(ingredients.keys()))
			amount = random.randint(ingredient_amount_min,ingredient_amount_max)
			multiplier = amount/ingredients[ing]['quantity']

			recipes[i][]