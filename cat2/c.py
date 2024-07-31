import numpy as np

x = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

def linear_interpolation(x, y, x_interp):
    i = np.searchsorted(x, x_interp) - 1
    return y[i] + (y[i+1] - y[i]) * (x_interp - x[i]) / (x[i+1] - x[i])

y_interp = linear_interpolation(x, y, 4.0)
print(f"Interpolated y value at x = 4.0: {y_interp}")
