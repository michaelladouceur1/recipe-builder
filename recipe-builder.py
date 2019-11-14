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

# SET TARGET MACROS INFO
target = {
    'calories': 2280,
    'meals': 3,
    'carb': 40,
    'fat': 200,
    'protein': 80
}

target['carbp'] = target['carb']/(target['carb'] + target['fat'] + target['protein'])
target['fatp'] = target['fat']/(target['carb'] + target['fat'] + target['protein'])
target['proteinp'] = target['protein']/(target['carb'] + target['fat'] + target['protein'])


# CREATE RECIPES AND POPULATE INFO
recipes = {}

def create_recipes():
    for i in range(recipe_count):
        recipes[i] = {
            'calories': 0,
            'ingredients': [],
            'quantity': 0,
            'carb': 0,
            'fat': 0,
            'protein': 0
        }

        ingredient_count = random.randint(ingredient_min,ingredient_max)

        for j in range(ingredient_count):
            ing = random.choice(list(ingredients.keys()))
            amount = random.randint(ingredient_amount_min,ingredient_amount_max)
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

def euclidean_dist(a,b):
    diff = [(i[0]-i[1])**2 for i in zip(a,b)]
    return sum(diff)**0.5

def local_min(a,b,error=0.001):
	for i in range(100):
		mid = (a+b)/2
		print(f'Mid {i+1}: {mid}')
		dist_mid = euclidean_dist([mid*i for i in source], target)
		dist_mid_p = euclidean_dist([(mid+1)*i for i in source], target)
		dist_mid_n = euclidean_dist([(mid-1)*i for i in source], target)
		diff_p = dist_mid_p - dist_mid
		diff_n = dist_mid_n - dist_mid
		print(f'Diff Plus: {diff_p}')
		print(f'Diff Neg: {diff_n}')
		print(f'Euc Dist: {dist_mid}\n')
		if abs(diff_p) > error and abs(diff_n) > error:
			if diff_p < diff_n:
				a = mid
			elif diff_p > diff_n:
				b = mid 
		else:
			break

if __name__ == '__main__':
	
	create_recipes()

	pp = pprint.PrettyPrinter(indent=2)
	pp.pprint(recipes)

	dist_sum = 0
	for i in range(len(recipes)):
	    dist = euclidean_dist([recipes[i]['carbp'],recipes[i]['fatp'],recipes[i]['proteinp']],
	                    [target['carbp'],target['fatp'],target['proteinp']])
	    print(f'Recipe {i}: {dist}')
	    dist_sum += dist
	    if i==0:
	        minimum = (i,dist)
	    else:
	        if dist < minimum[1]: 
	            minimum = (i,dist)

	print('\n')
	print(f'Distance Average: {dist_sum/recipe_count}')
	print(f'Minimum: {minimum}')
	# dot_prod()