import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 250)
X, Y = np.meshgrid(x, x)
a, b = 1, 1.5
c, d = 1.25, 1
Z1 = np.sin(-(X/a)**2-(Y/b)**2)
Z2 = np.sin(-(X/c)**2+(Y/d)**2)
plt.figure(1)
plt.imshow(Z1, cmap='Reds')
plt.figure(2)
plt.imshow(Z2, cmap='Reds')
plt.show()
