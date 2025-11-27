import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 5]
y = [0, 1, 2, 3, 4, 5, 20]

q = np.linspace(-np.pi, np.pi, 100)
plt.subplot(1, 2, 2)
for i in range(len(x)):
    r = x[i]*np.cos(q)+y[i]*np.sin(q)
    plt.plot(q, r)

plt.subplot(1, 2, 1)
plt.plot(x, y, 'o-')
plt.show()
