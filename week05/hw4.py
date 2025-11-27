import numpy as np

initial = np.array([[0], [1]])
D1 = 120
D2 = 220
D3 = 150

f1 = 100
f2 = 80

M1 = np.array([[1, 0], [-1/f1, 1]])
M2 = np.array([[1, 0], [-1/f2, 1]])

T1 = np.array([[1, D1], [0, 1]])
T2 = np.array([[1, D2], [0, 1]])
T3 = np.array([[1, D3], [0, 1]])

[x, a] = T3.dot(M2).dot(T2).dot(M1).dot(T1).dot(initial)

print(f'x = {x[0]}')
print(f'a = {a[0]}')
