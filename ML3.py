import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import model_selection, preprocessing, neural_network, metrics

# 1. Read dataset
df = pd.read_csv('Churn_Modelling.csv')

df.head()


# Drop irrelevant identifier columns
df = df.drop(columns=['RowNumber', 'CustomerId', 'Surname'])

# Encode categorical variables ('Geography' and 'Gender')
df = pd.get_dummies(df, drop_first=True)

df.head()


X = df.drop(columns=['Exited'])
y = df['Exited']

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42)


scaler = preprocessing.StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


model = neural_network.MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=100, random_state=42)
model.fit(X_train, y_train)


pred = model.predict(X_test)

print("Accuracy Score:", metrics.accuracy_score(y_test, pred))
print("\nClassification Report:\n", metrics.classification_report(y_test, pred))

sns.heatmap(metrics.confusion_matrix(y_test,pred),annot=True,fmt="d")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Bank Customer Churn Confusion Matrix")
plt.show()


