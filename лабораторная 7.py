import numpy as np 
B = np.array([[4, 1, 2], [0, 4, 3], [1, 1, 1]])
r = np.array([[-0.7], [1.3], [0.2]])
q = np.array([[-1.6], [0.8], [1.1]])
p = np.array([[0.1], [1.7], [-1.5]])

naillox = sum((B[i] * (r[i] - q[i]) * p[i] - r[i] for i in range(3)))

print("Скалярное произведение векторов:", naillox)
