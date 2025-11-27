import numpy as np
import matplotlib.pyplot as plt


def xNalpha(x0, a0, d1, f, d2):
    X0 = np.array([[x0], [a0]])
    T01 = np.array([[1, d1], [0, 1]])
    L1 = np.array([[1, 0], [-1/f, 1]])
    T12 = np.array([[1, d2], [0, 1]])
    xa = T12.dot(L1).dot(T01).dot(X0)
    return xa


H = []
f = 100
d1 = 300
d2 = 150
xobj = np.linspace(-5, 5, 100)
for x0 in xobj:
    if abs(x0) < 2:
        alpha = np.linspace(-5, 5, 1000)*np.pi/180
    else:
        alpha = np.linspace(-0.0005, 0.0005, 1000)*np.pi/180

    for a0 in alpha:
        Xf = xNalpha(x0, a0, d1, f, d2=100)
        if Xf[0] <= -0.001:
            continue
        X = xNalpha(x0, a0, d1, f, d2)
        H.append(X[0])
H = np.array(H)
bins = np.linspace(-10, 10, 50)
plt.hist(H, bins)
plt.show()
