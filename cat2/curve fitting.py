import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
x = np.linspace(0, 5, 50)
y = 2*x**2 + 3*x + 1 + np.random.normal(0, 1, 50)
def func(x, a, b, c):
    return a*x**2 + b*x + c
popt, pcov = curve_fit(func, x, y)
a, b, c = popt
print(f'The fitted curve is: y = {a:.2f}*x^2 + {b:.2f}*x + {c:.2f}')
plt.scatter(x, y, label='Data')
plt.plot(x, func(x, a, b, c), 'r-', label='Fitted Curve')
plt.legend()
plt.show()
