import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection, linear_model, ensemble, metrics

# 1. Load data and drop missing values
df = pd.read_csv('uber.csv').dropna()
df.head()

features = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count']


# 2. Filter unrealistic fares and passenger counts
df = df[(df['fare_amount'] > 0) & (df['fare_amount'] < 100)]
df = df[(df['passenger_count'] > 0) & (df['passenger_count'] <= 6)]

print("Cleaned shape:", df.shape)


# 3. Correlation check and plot
corr = df[features + ['fare_amount']].corr()
print("Correlation with fare amount:")
print(corr['fare_amount'])
# 3. Correlation check and plot
#corr = df.corr(numeric_only=True)
#print(corr['fare_amount'])

plt.matshow(corr)
plt.title("Correlation Matrix")
plt.colorbar()
plt.show()


# 4. Train-test split and model fitting
X = df[features]
y = df['fare_amount']

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42)

lr = linear_model.LinearRegression().fit(X_train, y_train)
rf = ensemble.RandomForestRegressor(n_estimators=10, max_depth=5, random_state=42).fit(X_train, y_train)

print("Models trained successfully.")


# 5. Evaluate R2, RMSE (without numpy using ** 0.5), and plot predictions
for name, model in [('Linear Regression', lr), ('Random Forest', rf)]:
    pred = model.predict(X_test)
    
    print(name)
    print("R2 Score :", metrics.r2_score(y_test, pred))
    print("RMSE     :", metrics.mean_squared_error(y_test, pred) ** 0.5)
    
    # Graphic: Actual vs Predicted
    plt.scatter(y_test[:100], pred[:100])
    plt.xlabel("Actual Fare")
    plt.ylabel("Predicted Fare")
    plt.title(f"{name}: Actual vs Predicted")
    plt.show()
