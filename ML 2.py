import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection, neighbors, svm, metrics
# 1. Load dataset
df = pd.read_csv('emails.csv')

df.head()


# Drop the text ID column, separate features (X) and target (y: 'Prediction')
X = df.drop(columns=['Email No.', 'Prediction'])
y = df['Prediction']

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42)

knn = neighbors.KNeighborsClassifier()
svc = svm.SVC()

for name, model in [('KNN', knn), ('SVM', svc)]:
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    
    print(f"\n--- {name} ---")
    print("Accuracy Score:", metrics.accuracy_score(y_test, pred))
    print(metrics.classification_report(y_test, pred))
    
    # Plot Confusion Matrix
    metrics.ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
    plt.show()
    
