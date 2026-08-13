import numpy as np
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.neural_network import MLPRegressor


X = np.array([
    [1], [2], [3], [4], [5],
    [6], [7], [8], [9], [10]
])

y = np.array([
    2, 4, 6, 8, 10,
    12, 14, 16, 18, 20
])


linear_model = LinearRegression()

random_forest_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

xgboost_model = XGBRegressor(
    n_estimators=100,
    random_state=42
)

neural_network_model = MLPRegressor(
    hidden_layer_sizes=(64, 32),
    max_iter=1000,
    random_state=42
)


linear_model.fit(X, y)
random_forest_model.fit(X, y)
xgboost_model.fit(X, y)
neural_network_model.fit(X, y)


joblib.dump(linear_model, "models/linear_model.joblib")
joblib.dump(random_forest_model, "models/random_forest_model.joblib")
joblib.dump(xgboost_model, "models/xgboost_model.joblib")
joblib.dump(neural_network_model, "models/neural_network_model.joblib")

print("All models trained and saved successfully!")