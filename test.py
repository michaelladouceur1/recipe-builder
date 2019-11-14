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


# print(minimum)

# print(euclidean_dist(target, source))

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

		# if diff_p < diff_n:
		# 	a = mid
		# elif diff_p > diff_n:
		# 	b = mid 


local_min(100,2500)