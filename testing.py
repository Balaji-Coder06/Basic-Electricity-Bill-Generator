import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset (Example: temperature data)
data = pd.read_csv("climate_data.csv")  # Assume CSV contains year, temperature, CO2 levels, humidity, etc.

# Select features and target variable
X = data[['CO2', 'Humidity', 'Year']]
y = data['Temperature']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
error = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {error}")

# Predict future temperature
future_data = np.array([[420, 70, 2030]])  # Example input for year 2030
future_temp = model.predict(future_data)
print(f"Predicted Temperature in 2030: {future_temp[0]}")
