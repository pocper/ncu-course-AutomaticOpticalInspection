import numpy as np

data = []
total = []
dx = 0.1

for i in range(6):
    data.append(np.loadtxt(f'聚焦度值練習/g{i}t.txt'))
    dydx = (abs(data[i][1:len(data[i])]-data[i][0:len(data[i])-1])/dx)
    total.append(int(sum(dydx)))

print(f'g{total.index(max(total))}t.txt')