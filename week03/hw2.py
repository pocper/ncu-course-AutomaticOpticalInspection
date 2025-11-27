import matplotlib.pyplot as plt
import numpy as np


def func(x):
    return x**0.5


def diff_func(x):
    return 1/(2*(x**0.5))


class vector:
    a = []
    b = []
    c = []
    pt = []

    def __init__(self, pt, a):
        self.a = a
        self.pt = pt
        self.b = self.const_multiply(
            self.dot(self.a, self.normalize([1, -1/diff_func(pt[0])])),
            self.normalize([1, -1/diff_func(pt[0])])
        )
        self.c = self.minus(self.a, self.const_multiply(2, self.b))

    def add(self, a, b):
        return [a[0]+b[0], a[1]+b[1]]

    def minus(self, a, b):
        return [a[0]-b[0], a[1]-b[1]]

    def const_multiply(self, a, b):
        return [a*b[0], a*b[1]]

    def dot(self, a, b):
        return a[0]*b[0]+a[1]*b[1]

    def length(self, a):
        return (a[0]**2+a[1]**2)**0.5

    def normalize(self, a):
        return [a[0]/self.length(a), a[1]/self.length(a)]

    def slope(self, a):
        return a[1]/a[0]

    def reflect(self, x):
        return self.slope(self.c)*(x-self.pt[0])+self.pt[1]


x = np.linspace(0, 0.5, 100)
plt.plot(x, func(x))

h1, h2, h3 = 0.01, 0.05, 0.10
incident_line_vec = [-1, 0]

x1 = np.linspace(h1, 0.5, 100)
x2 = np.linspace(h2, 0.5, 100)
x3 = np.linspace(h3, 0.5, 100)


vec1 = vector([h1, func(h1)], incident_line_vec)
plt.plot(x1, vec1.reflect(x1))

vec2 = vector([h2, func(h2)], incident_line_vec)
plt.plot(x2, vec2.reflect(x2))

vec3 = vector([h3, func(h3)], incident_line_vec)
plt.plot(x3, vec3.reflect(x3))

plt.xlim([0, 0.3])
plt.ylim([-0.1, 0.4])
plt.grid()
plt.show()
