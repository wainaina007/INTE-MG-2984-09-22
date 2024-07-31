import numpy as np
def f(x):
    return x**2
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return integral
a = 0
b = 1
n = 100
result = trapezoidal_rule(a, b, n)
print(f"The integral of f(x) from {a} to {b} is approximately {result}")
