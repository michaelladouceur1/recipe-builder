import numpy as np

a = np.array([[3,1,2], [1,2,0], [5,3,4]])
b = np.array([9,8,4])
x = np.linalg.solve(a, b)
print(x)