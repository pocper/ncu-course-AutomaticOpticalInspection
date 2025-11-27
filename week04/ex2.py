import numpy as np

ni = eval(input('入射介質折射率:'))
nr = eval(input('折射介質折射率:'))
qi = eval(input('入射角[deg]:'))

qr = np.arcsin(ni/nr*np.sin(qi*np.pi/180))*180/np.pi
totalReflection = np.sin(ni/nr)

if(qi > totalReflection*180/np.pi):
    print(f'反射角[deg]:{qi}')
else:
    print(f'折射角[deg]:{qr}')
