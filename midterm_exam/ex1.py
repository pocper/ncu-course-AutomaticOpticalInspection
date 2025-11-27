import numpy as np
import matplotlib.pyplot as plt

# keyboard input
n = float(input('輸入稜鏡折射率 n = '))
A = float(input('輸入頂角角度 A [deg] = '))

# global variable
theta1 = np.linspace(0, 90, 100)
rad2deg = 180/np.pi
deg2rad = np.pi/180

# calculate the angle
D = theta1-A+np.arcsin(np.sqrt(n**2-(np.sin(theta1*deg2rad))**2)
                       * np.sin(A*deg2rad)-np.sin(theta1*deg2rad)*np.cos(A*deg2rad))*rad2deg

# plot the result
plt.plot(theta1, D)
plt.xlim([0, 90])
plt.xlabel('theta1[deg]')
plt.ylabel('D[deg]')
plt.show()
