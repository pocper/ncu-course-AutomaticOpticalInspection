print('Calculate the distance of p1 and p2')
print('Enter p1(x1,y1):')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

print('Enter p2(x2,y2):')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

print(f'The distance between ({x1},{y1}) and ({x2},{y2}) is {((y2-y1)**2+(x2-x1)**2)**0.5}')