import numpy as np
X_0 = 1
alpha = 1*np.pi/180
n = 1.0
n_p = 1.5
R = 15

alpha_p = -((n_p-n)/R)*(X_0/n_p)+(n/n_p)*alpha
print(alpha_p*180/np.pi)
