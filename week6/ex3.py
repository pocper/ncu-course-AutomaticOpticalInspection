import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
T = np.linspace(-10, 10, 100)
Y = np.zeros(len(T))
dx = (10-(-10))/200

# plt.figure(1)
for i in range(0, len(T)):
    t = T[i]
    y0 = np.exp(-(t-x)**2)
    y0[np.where(y0 > 0.2)] = 1
    y0[np.where(y0 <= 0.2)] = 0
    y1 = np.exp(-(x+2)**2)+np.exp(-(x-2)**2)
    Y[i] = np.sum(y1*y0)*dx

    plt.figure(1)
    plt.clf()
    plt.plot(x, y0, x, y1)
    plt.axis([-10, 10, 0, 3])
    plt.draw()

    plt.figure(2)
    plt.plot(x[i], Y[i], "o")
    plt.axis([-10, 10, 0, 3])
    plt.draw()

plt.show()
