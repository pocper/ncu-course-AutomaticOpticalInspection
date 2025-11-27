import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-30, 30, 500)
X, Y = np.meshgrid(x, x)

z = 5
L = 0.5
c1 = (1, 1, z)
c2 = (-1, -1, z)

r1 = np.sqrt((c1[0]-X)**2+(c1[1]-Y)**2+c1[2]**2)
r2 = np.sqrt((c2[0]-X)**2+(c2[1]-Y)**2+c2[2]**2)
k = 2*np.pi/L
E1 = np.exp(1j*k*r1)
E2 = np.exp(1j*k*r2)
I = abs(E1+E2)**2
plt.imshow(I, cmap='Reds')
plt.show()
