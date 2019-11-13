import random
import math
import pprint

ingredients = {
    'chicken': {
        'quantity': 100,
        'units': 'grams',
        'carbs': 0,
        'fat': 3.6,
        'protein': 31
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
        'carbs': 17,
        'fat': 0.1,
        'protein': 2
    },
    'carrots': {
        'quantity': 100,
        'units': 'grams',
        'carbs': 12.26,
        'fat': 0.31,
        'protein': 1.19
    },
    'avocado': {
        'quantity': 100,
        'units': 'grams',
        'carbs': 9,
        'fat': 15,
        'protein': 2
    },
    'rice': {
        'quantity': 100,
        'units': 'grams',
        'carbs': 35,
        'fat': 0.3,
        'protein': 2.7
    },
    'beef': {
        'quantity': 100,
        'units': 'grams',
        'carbs': 0,
        'fat': 15,
        'protein': 26
    },
    'peas': {
        'quantity': 100,
        'units': 'grams',
        'carbs': 14,
        'fat': 0.4,
        'protein': 5
    }
}

target = {
    'calories': 2500,
    'carbs': 100,
    'fat': 200,
    'protein': 200
}
target['carbsp'] = target['carbs']/(target['carbs'] + target['fat'] + target['protein'])
target['fatp'] = target['fat']/(target['carbs'] + target['fat'] + target['protein'])
target['proteinp'] = target['protein']/(target['carbs'] + target['fat'] + target['protein'])

recipes = {}

def print_ing():
    for ing in ingredients:
        print(f'\nIngredient: {ing}')
        for item in ingredients[ing]:
            print(f'{item}: {ingredients[ing][item]}')

def create_recipes():
    for i in range(25):
        recipes[i] = {
            'calories': 0,
            'ingredients': [],
            'quantity': 0,
            'carbs': 0,
            'fat': 0,
            'protein': 0
        }
        count = random.randint(1,10)
        for j in range(count):
            ing = random.choice(list(ingredients.keys()))
            amount = random.randint(25,100)
            multiplier = amount/ingredients[ing]['quantity']
    
            recipes[i]['ingredients'].append({'name': ing, 'quantity': amount})
            recipes[i]['ingredients'][j]['quantity'] = amount
            recipes[i]['quantity'] += amount
            recipes[i]['carbs'] += multiplier*ingredients[ing]['carbs']
            recipes[i]['fat'] += multiplier*ingredients[ing]['fat']
            recipes[i]['protein'] += multiplier*ingredients[ing]['protein']

        recipes[i]['calories'] = recipes[i]['carbs']*4 + recipes[i]['fat']*9 + recipes[i]['protein']*4
        recipes[i]['calpg'] = recipes[i]['calories']/recipes[i]['quantity']
        recipes[i]['carbpg'] = recipes[i]['carbs']/(recipes[i]['carbs'] + recipes[i]['fat'] + recipes[i]['protein'])
        recipes[i]['fatpg'] = recipes[i]['fat']/(recipes[i]['carbs'] + recipes[i]['fat'] + recipes[i]['protein'])
        recipes[i]['proteinpg'] = recipes[i]['protein']/(recipes[i]['carbs'] + recipes[i]['fat'] + recipes[i]['protein'])

def euclidean_dist():
    for i in range(len(recipes)):
        # cal_diff = (recipes[i]['calpg'] - recipes[i+1]['calpg'])
        # carb_diff = (recipes[i]['carbpg'] - recipes[i+1]['carbpg'])
        # fat_diff = (recipes[i]['fatpg'] - recipes[i+1]['fatpg'])
        # protein_diff = (recipes[i]['proteinpg'] - recipes[i+1]['proteinpg'])
        # cal_diff = (recipes[i]['calpg'] - target['calories'])
        carb_diff = (recipes[i]['carbpg'] - target['carbsp'])
        fat_diff = (recipes[i]['fatpg'] - target['fatp'])
        protein_diff = (recipes[i]['proteinpg'] - target['proteinp'])

        dist = math.sqrt((carb_diff**2) + (fat_diff**2) + (protein_diff**2))
        print(f'Distance from Recipe {i} to Target: {dist}')

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
# dot_prod()