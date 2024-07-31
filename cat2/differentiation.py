import numpy as np
import sympy as sp
x = sp.Symbol('x')
f = x**3 + 2*x**2 - 5*x + 1
df = sp.diff(f, x)
print(f'The derivative of the function is: {df}')
