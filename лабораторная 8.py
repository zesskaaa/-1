import numpy as np 
N=3

A = np.array([[1, 5, 1], [4, -1, 1], [25, 6, 64]])
B = np.array([30, 21, 1253])


x = np.linalg.inv(A).dot(B)
print('')
print('X')
for i in range (0,N):
    print('%f'%x[i],end=' ')
print('')

x1 = np.linalg.solve(A,B)
print('')
print('X1')

for i in range (0,N):
    print('%f'%x1[i],end=' ')
print('')
print('\nDet(A)=%f'%np.linalg.det(A))
