import numpy as np
def f(x):
    return x**3 + 2*x**2 - 5*x + 1
a = 0
b = 2
n = 100
h = (b - a) / n
integral = (f(a) + f(b)) / 2
for i in range(1, n):
    x = a + i*h
    integral += f(x)
integral *= h
print(f'The numerical integral of the function is: {integral}')
