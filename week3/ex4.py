from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

O_x, O_y = -1, 2
A_x, A_y = -2, 0
B_x, B_y = 0, 1

range_mirror = np.linspace(-3, 1, 1000)
range_OA = np.linspace(A_x, O_x, 1000)
range_OB = np.linspace(O_x, B_x, 1000)
range_reflect = np.linspace(-3, 1, 1000)
slope_OA = (A_y-O_y)/(A_x-O_x)
slope_OB = (B_y-O_y)/(B_x-O_x)

plt.plot(range_mirror, (range_mirror+2)/2)
plt.plot(range_OA, slope_OA*range_OA+4)
plt.plot(range_OB, -range_OB+1)
plt.plot(range_reflect, -0.1818*range_reflect-0.3636)
plt.plot(range_reflect, -7*range_reflect+1)

Intersection_x = A_x
Intersection_y = A_y
epsilon = 0.01

for x in range_reflect:
    y1 = -0.1818*x-0.3636
    y2 = -7*x+1

    if abs(y2-y1) < epsilon:
        Intersection_x = x
        Intersection_y = y1
        break

plt.plot(Intersection_x, Intersection_y, 'o')
plt.text(0.25, -0.3, f'({round(Intersection_x,1)}, {round(Intersection_y,1)})')

plt.plot(A_x, A_y, 'o')
plt.text(A_x-0.1, A_y+0.1, f'({A_x}, {A_y})')

plt.plot(B_x, B_y, 'o')
plt.text(B_x+0.05, B_y+0.2, f'({B_x}, {B_y})')

plt.plot(O_x, O_y, 'o')
plt.text(O_x-0.1, O_y+0.1, f'({O_x}, {O_y})')

plt.xlim([-2.5, 0.5])
plt.ylim([-1, 2.5])
plt.grid()
plt.show()
