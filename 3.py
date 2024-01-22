import cmath
a, b, c = map(float, input("Введіть a, b, c : ").split())
delta = cmath.sqrt(b**2 - 4*a*c)
root1 = (-b + delta) / (2*a)
root2 = (-b - delta) / (2*a)
print("Корені рівняння:", root1, root2)
