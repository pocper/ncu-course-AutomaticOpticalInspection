import numpy as np
import matplotlib.pyplot as plt
limit = 20
focus = 100
N = 100
dA = (2*limit/N)**2
X = np.linspace(-limit, limit, N)
Y = np.linspace(-limit, limit, N)
S = np.linspace(0, focus, N)
def a(s): return 10+10*s/100
def b(s): return 20-10*s/100


FES = []

for s in S:
    A, B, C, D = 0, 0, 0, 0
    for x in X:
        for y in Y:
            if(x**2/a(s)**2+y**2/b(s)**2 <= 1):
                if(x+y > 0 and x-y < 0):
                    A += dA
                if(x+y > 0 and x-y > 0):
                    B += dA
                if(x+y < 0 and x-y > 0):
                    C += dA
                if(x+y < 0 and x-y < 0):
                    D += dA
    FES.append(((A+C)-(B+D))/(A+B+C+D))

plt.plot(S, FES)
plt.xlabel('Position')
plt.ylabel('FES')
plt.grid()
plt.show()
