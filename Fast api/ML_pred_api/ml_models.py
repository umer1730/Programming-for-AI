from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

from sklearn.neural_network import MLPRegressor

#linear regression
linear_model = LinearRegression()

#random forest
random_forest_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# XGBoost
xgboost_model = XGBRegressor(
    n_estimators = 100,
    random_state = 42
)

#neural network
neural_network_model = MLPRegressor(
    hidden_layer_sizes=(64,32),
    max_iter = 1000,
    random_state = 42
)