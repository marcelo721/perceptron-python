import numpy as np

entradas = np.array([1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def sum(e, p):
    return e.dot(p) #dot product

def stepFunction(sum):
    if sum >= 1:
        return 1
    return 0


s = sum(entradas, pesos)
print(s)

result = stepFunction(s)
print(result)
