import numpy as np

coefficients = [2, -8, 6, -4, 2]
poly = np.poly1d(coefficients)
roots = np.roots(coefficients)
derivative = poly.deriv()
second_derivative = poly.deriv(2)
value_at_50 = poly(50)

print(f'''
Поліном = {poly}\n
Корені полінома = {roots}\n
Похідна полінома = {derivative}\n
Друга похідна полінома = {second_derivative}\n
Значення при n=50 = {value_at_50}
''')
