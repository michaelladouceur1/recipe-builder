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
    }
}

target = {
    'calories': 2500,
    'carb': 100,
    'fat': 200,
    'protein': 200
}
target['carbp'] = target['carb']/(target['carb'] + target['fat'] + target['protein'])
target['fatp'] = target['fat']/(target['carb'] + target['fat'] + target['protein'])
target['proteinp'] = target['protein']/(target['carb'] + target['fat'] + target['protein'])

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
            'carb': 0,
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
            recipes[i]['carb'] += multiplier*ingredients[ing]['carb']
            recipes[i]['fat'] += multiplier*ingredients[ing]['fat']
            recipes[i]['protein'] += multiplier*ingredients[ing]['protein']

        recipes[i]['calories'] = recipes[i]['carb']*4 + recipes[i]['fat']*9 + recipes[i]['protein']*4
        recipes[i]['calpg'] = recipes[i]['calories']/recipes[i]['quantity']
        recipes[i]['carbp'] = recipes[i]['carb']/(recipes[i]['carb'] + recipes[i]['fat'] + recipes[i]['protein'])
        recipes[i]['fatp'] = recipes[i]['fat']/(recipes[i]['carb'] + recipes[i]['fat'] + recipes[i]['protein'])
        recipes[i]['proteinp'] = recipes[i]['protein']/(recipes[i]['carb'] + recipes[i]['fat'] + recipes[i]['protein'])

# def euclidean_dist():
#     minn = 100
#     for i in range(len(recipes)):
#         carb_diff = (recipes[i]['carbp'] - target['carbp'])
#         fat_diff = (recipes[i]['fatp'] - target['fatp'])
#         protein_diff = (recipes[i]['proteinp'] - target['proteinp'])
        
#         dist = math.sqrt((carb_diff**2) + (fat_diff**2) + (protein_diff**2))
#         print(f'Distance from Recipe {i} to Target: {dist}')

def euclidean_dist(a,b):
    diff = [(i[0]-i[1])**2 for i in zip(a,b)]
    return sum(diff)**0.5


def dot_prod():
    for i in range(len(recipes)-1):
        cal = (recipes[i]['calories']/recipes[i]['quantity']) * (recipes[i+1]['calories']/recipes[i+1]['quantity'])
        carb = (recipes[i]['carb']/recipes[i]['quantity']) * (recipes[i+1]['carb']/recipes[i+1]['quantity'])
        fat = (recipes[i]['fat']/recipes[i]['quantity']) * (recipes[i+1]['fat']/recipes[i+1]['quantity'])
        protein = (recipes[i]['protein']/recipes[i]['quantity']) * (recipes[i+1]['protein']/recipes[i+1]['quantity'])

        dot = cal + carb + fat + protein
        print(f'Dot for {i} and {i+1}: {dot}')

create_recipes()
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(recipes)
for i in range(len(recipes)):
    dist = euclidean_dist([recipes[i]['carbp'],recipes[i]['fatp'],recipes[i]['proteinp']],
                    [target['carbp'],target['fatp'],target['proteinp']])
    print(f'Recipe {i}: {dist}')
    if i==0:
        minimum = (i,dist)
    else:
        if dist < minimum[1]: 
            minimum = (i,dist)

print('\n')
print(f'Minimum: {minimum}')
# dot_prod()