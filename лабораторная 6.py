m = 5
A = [1, -2, 3, -4, 5][:m]
B = [-1, 2, -3, 4, -5][:m]

K = []
for i in range(m):
    if A[i]*B[i] < 0:
        K.append(-1)
    elif A[i]*B[i] > 0:
        K.append(1)

print("Массив A:", A)
print("Массив B:", B)
print("Сформированный массив K по правилу:", K)
