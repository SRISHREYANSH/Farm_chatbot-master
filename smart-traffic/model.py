import numpy as np
from sklearn.linear_model import LinearRegression

# Training data (Hour vs Traffic Density)
X = np.array([6, 7, 8, 9, 10, 12, 15, 17, 18, 19, 20]).reshape(-1, 1)
y = np.array([20, 40, 80, 100, 60, 50, 65, 90, 120, 110, 70])

# Train model
model = LinearRegression()
model.fit(X, y)

def predict_traffic(hour):
    prediction = model.predict([[hour]])
    return int(prediction[0])
