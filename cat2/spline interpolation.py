import numpy as np
from scipy.interpolate import interp1d
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 11, 9, 17, 23])
f = interp1d(x, y, kind='cubic')
x_new = np.linspace(1, 5, 50)
y_new = f(x_new)
import matplotlib.pyplot as plt
plt.scatter(x, y, label='Original Data')
plt.plot(x_new, y_new, 'r-', label='Spline Interpolation')
plt.legend()
plt.show()
