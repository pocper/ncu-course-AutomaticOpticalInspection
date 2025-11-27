import numpy as np
import matplotlib.pyplot as plt

p = ['A', 'B', 'C', 'D', 'E', 'F']
x = [0, 1, 2, 3, 2, 4, 6]
y = [0, 1, 2, 3, 3, 4, 5]

Q = np.linspace(-np.pi/2, np.pi/2, 500)
R_interval = np.linspace(-10, 10, 500)
dR = (max(R_interval)-min(R_interval))/len(R_interval)
r = np.zeros(len(p))
for q in Q:
    for i in range(len(p)):
        r[i] = x[i]*np.cos(q)+y[i]*np.sin(q)
    box = []

    for R in R_interval:
        for i in range(len(p)):
            if(r[i] > R and r[i] < R+dR):
                box.append(p[i])

        if(len(box) > 3):
            print(box)
        else:
            box = []
        box = []
