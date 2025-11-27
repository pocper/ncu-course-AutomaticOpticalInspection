import numpy as np
na = 1
ng = 1.5
A = 30*np.pi/180
q1 = np.linspace(0, 90, 3000)*np.pi/180
q1p = np.arcsin(na*np.sin(q1)/ng)
q2 = A-q1p
q2p = np.arcsin(ng*np.sin(q2)/na)
D = q1+q2p-A

min_delfection_radian = 90
min_incident_radian = 0

for i in D:
    if(i < min_delfection_radian):
        min_delfection_radian = i

min_incident_radian = q1[D.tolist().index(min_delfection_radian)]

print(f'最小偏轉角[deg]:{min_delfection_radian*180/np.pi}')
print(f'對應入射角[deg]:{min_incident_radian*180/np.pi}')
