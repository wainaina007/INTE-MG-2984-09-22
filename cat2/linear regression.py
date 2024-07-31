import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1, 2], [1, 4], [2, 2], [2, 4], [3, 6]])
y = np.array([5, 11, 9, 17, 23])
model = LinearRegression()
model.fit(X, y)
print(f'The slope is: {model.coef_}')
print(f'The intercept is: {model.intercept_}')
