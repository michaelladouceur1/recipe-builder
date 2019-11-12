import random
import math
import pprint

ingredients = {
    'chicken': {
        'quantity': 100,
        'units': 'grams',
        'carbs': 0,
        'fat': 9,
        'protein': 25
    },
    'olive oil': {
        'quantity': 28,
        'units': 'grams',
        'carbs': 0,
        'fat': 28,
        'protein': 0
    },
    'potatoes': {
        'quantity': 100,
        'units': 'grams',
        'carbs': 35,
        'fat': 1,
        'protein': 3
    },
    'carrots': {
        'quantity': 100,
        'units': 'grams',
        'carbs': 28,
        'fat': 0,
        'protein': 1
    },
    'avocado': {
        'quantity': 100,
        'units': 'grams',
        'carbs': 8,
        'fat': 23,
        'protein': 2
    },
    'rice': {
        'quantity': 100,
        'units': 'grams',
        'carbs': 45,
        'fat': 0,
        'protein': 2
    },
    'beef': {
        'quantity': 100,
        'units': 'grams',
        'carbs': 0,
        'fat': 18,
        'protein': 30
    },
    'peas': {
        'quantity': 100,
        'units': 'grams',
        'carbs': 22,
        'fat': 1,
        'protein': 9
    }
}

recipes = {}

def print_ing():
    for ing in ingredients:
        print(f'\nIngredient: {ing}')
        for item in ingredients[ing]:
            print(f'{item}: {ingredients[ing][item]}')

def create_recipes():
    for i in range(10):
        recipes[i] = {
            'calories': 0,
            'ingredients': [],
            'quantity': 0,
            'carbs': 0,
            'fat': 0,
            'protein': 0
        }
        count = random.randint(1,7)
        for j in range(count):
            ing = random.choice(list(ingredients.keys()))
            amount = random.randint(25,200)
            multiplier = amount/ingredients[ing]['quantity']
    
            recipes[i]['ingredients'].append({'name': ing, 'quantity': amount})
            recipes[i]['ingredients'][j]['quantity'] = amount
            recipes[i]['quantity'] += amount
            recipes[i]['carbs'] += multiplier*ingredients[ing]['carbs']
            recipes[i]['fat'] += multiplier*ingredients[ing]['fat']
            recipes[i]['protein'] += multiplier*ingredients[ing]['protein']

        recipes[i]['calories'] = recipes[i]['carbs']*4 + recipes[i]['fat']*9 + recipes[i]['protein']*4

def euclidean_dist():
    for i in range(len(recipes)-1):
        cal_diff = (recipes[i]['calories']/recipes[i]['quantity']) - (recipes[i+1]['calories']/recipes[i+1]['quantity'])
        carb_diff = (recipes[i]['carbs']/recipes[i]['quantity']) - (recipes[i+1]['carbs']/recipes[i+1]['quantity'])
        fat_diff = (recipes[i]['fat']/recipes[i]['quantity']) - (recipes[i+1]['fat']/recipes[i+1]['quantity'])
        protein_diff = (recipes[i]['protein']/recipes[i]['quantity']) - (recipes[i+1]['protein']/recipes[i+1]['quantity'])

        dist = math.sqrt((cal_diff**2) + (carb_diff**2) + (fat_diff**2) + (protein_diff**2))
        print(f'Distance from {i} to {i+1}: {dist}')

def dot_prod():
    for i in range(len(recipes)-1):
        cal = (recipes[i]['calories']/recipes[i]['quantity']) * (recipes[i+1]['calories']/recipes[i+1]['quantity'])
        carb = (recipes[i]['carbs']/recipes[i]['quantity']) * (recipes[i+1]['carbs']/recipes[i+1]['quantity'])
        fat = (recipes[i]['fat']/recipes[i]['quantity']) * (recipes[i+1]['fat']/recipes[i+1]['quantity'])
        protein = (recipes[i]['protein']/recipes[i]['quantity']) * (recipes[i+1]['protein']/recipes[i+1]['quantity'])

        dot = cal + carb + fat + protein
        print(f'Dot for {i} and {i+1}: {dot}')

create_recipes()
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(recipes)
euclidean_dist()
print('\n')
dot_prod()