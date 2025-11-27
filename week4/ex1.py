import numpy as np
import matplotlib.pyplot as plt

t = 5
ni = 1
nr = 1.5


def rad2deg(rad):
    return rad*180/np.pi


theta_i = np.linspace(0, np.pi/2, 100)
theta_r = np.arcsin(ni/nr*np.sin(theta_i))
d = t/np.cos(theta_r)*np.sin(theta_i-theta_r)

plt.xlim([0, 90])
plt.xlabel('incident degree[deg]')
plt.ylabel('d')
plt.plot(rad2deg(theta_i), d)
plt.grid()
plt.show()
