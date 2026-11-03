import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model, ensemble, model_selection, metrics
import seaborn as sns

df=pd.read_csv("uber.csv")
df.head()


df.shape


df=df[["fare_amount","pickup_longitude"	,"pickup_latitude"	,"dropoff_longitude"	,"dropoff_latitude"	,"passenger_count"]]
df=df[(df["fare_amount"]>0) & (df["fare_amount"]<100)]
df=df[(df["passenger_count"]>0) & (df["passenger_count"]<=6)]
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)

IQR = Q3 - Q1

df = df[~((df < (Q1 - 1.5 * IQR)) |
          (df > (Q3 + 1.5 * IQR))).any(axis=1)]

df.shape
df.shape


sns.heatmap(df.corr(),annot=True)
df.corr()


X=df.drop(columns=['fare_amount'])
y=df['fare_amount']

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2,random_state=42)


lr=linear_model.LinearRegression()
lr.fit(X_train,y_train)

rf=ensemble.RandomForestRegressor(n_estimators=10, max_depth=5 , random_state=42 )
rf.fit(X_train,y_train)



for name, model in [('Linear Regression',lr),('Random FOrest', rf)]:
    print(name)
    pred=model.predict(X_test)
    print("R2 score= ", metrics.r2_score(y_test,pred))
    print("RMSE= ", metrics.mean_squared_error(y_test,pred))

    plt.scatter(y_test[:100],pred[:100])
    plt.show()
