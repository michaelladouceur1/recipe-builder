import numpy as np
import random
import math

# a = np.array([[0.202,0.566,0.042], [.047,0.003,0.462], [.020,0.0119,0.106]])
# carbs = 10
# fat = 10
# protein = 10

# for i in range(1000):
#     c = random.randint(carbs*0.5, carbs*2)
#     f = random.randint(fat*0.5, fat*2)
#     p = random.randint(protein*0.5, protein*2)
#     b = np.array([c,f,p])
#     x = np.linalg.solve(a, b)
#     print(x)

def euclidean_dist(a,b):
    diff = [(i[0]-i[1])**2 for i in zip(a,b)]
    return sum(diff)**0.5
    

# dist = euclidean_dist([0,8,23], [6,2,0])
# print(dist)

def equation_solver(*args,answer):
	a = np.array([*args])
	b = np.array(answer)
	x = np.linalg.solve(a,b)
	return x

# ans = equation_solver([10,30,40], [50,40,30], [40,30,30], answer=[20,40,40])
# print(ans)

accur = 20

target = [100,200,200]
source = [.165,.527,.308]
# source = [.05,.25,.3]
# source = [(target[0]-accur)/1000,(target[1]-accur)/1000,(target[2]-accur)/1000]

# for m in range(100,1000):
# 	dist = euclidean_dist(target, [m*i for i in source])
# 	print(f'{m} grams: {dist}')
# 	if m == 100:
# 		minimum = (dist,m)
# 	else:
# 		if dist < minimum[0]:
# 			minimum = (dist,m)

def local_min(func,a=0,b=10):
	def inner(*args):
		low = a
		up = b
		mid_prev = low
		for i in range(100):
			error=0.001
			step=0.001
			mid = (low+up)/2

			y = func(mid)
			yp = func(mid+step)
			yn = func(mid-step)
			print(f'Step {i+1}')
			print(f'Mid: {mid}')
			print(f'Y: {y}')
			print(f'Yp: {yp}')
			print(f'Yn: {yn}')
			print(f'Diff: {abs(mid_prev-mid)}\n')
			diff_p = yp - y
			diff_n = yn - y

			if i==0 or abs(mid_prev-mid) > error:
				if diff_p < diff_n:
					low = mid
				elif diff_p > diff_n:
					up = mid 
			else:
				break

			mid_prev = mid


		return mid
	return inner

def parab(x):
	return 1/x**2

# print(minimum)

# print(euclidean_dist(target, source))

		# if diff_p < diff_n:
		# 	a = mid
		# elif diff_p > diff_n:
		# 	b = mid 

function = local_min(func=parab,a=-3,b=10)

x = function()
print(x)