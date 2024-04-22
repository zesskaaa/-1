import sympy as sp

x = sp.Symbol('x')

f = 2*x**4 - 8*x**3 - 9*x**2 - 14*x + 2

f_prime = f.diff(x)

extremum_points = sp.solve(f_prime, x)

extremum_points += [-5, 5]

values = [f.subs(x, point) for point in extremum_points]

max_value = max(values)
min_value = min(values)

print("Наибольшее значение функции на отрезке [-5;5]:", max_value)
print("Наименьшее значение функции на отрезке [-5;5]:", min_value)
