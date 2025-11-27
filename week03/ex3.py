a1, b1, c1 = 5, 3, 10
a2, b2, c2 = 3, 5, 5

delta = a1*b2-b1*a2
delta_x = c1*b2-b1*c2
delta_y = a1*c2-c1*a2

x = delta_x/delta
y = delta_y/delta
print(f'Intersection of L1(5x+3y=10), L2(3x+5y=5) is ({x},{y})')
