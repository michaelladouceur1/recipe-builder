import numpy as np
import random

a = np.array([[0.202,0.566,0.042], [.047,0.003,0.462], [.020,0.0119,0.106]])
carbs = 10
fat = 10
protein = 10

for i in range(1000):
    c = random.randint(carbs*0.5, carbs*2)
    f = random.randint(fat*0.5, fat*2)
    p = random.randint(protein*0.5, protein*2)
    b = np.array([c,f,p])
    x = np.linalg.solve(a, b)
    print(x)