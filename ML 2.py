import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection, neighbors, svm, metrics
import seaborn as sns

# 1. Load dataset
df = pd.read_csv('emails.csv')

df.head()


# Drop the text ID column, separate features (X) and target (y: 'Prediction')
X = df.drop(columns=['Email No.', 'Prediction'])
y = df['Prediction']

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42)


knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)


svc = svm.SVC()
svc.fit(X_train, y_train)


for name, model in [('KNN', knn), ('SVM', svc)]:
    pred = model.predict(X_test)
    
    print(f"\n--- {name} ---")
    print("Accuracy Score:", metrics.accuracy_score(y_test, pred))
    print(metrics.classification_report(y_test, pred))
    
    # Plot Confusion Matrix
    sns.heatmap(metrics.confusion_matrix(y_test,pred),annot=True,fmt="d")
    plt.show()


from sklearn.feature_extraction.text import TfidfVectorizer

texts = [
    "free lottery winner",
    "claim your prize now",
    "win money today",
    "meeting schedule project",
    "project discussion",
    "team meeting tomorrow"
]

labels = [1,1,1,0,0,0]

tfidf = TfidfVectorizer()
X = tfidf.fit_transform(texts)

knn.fit(X, labels)
svc.fit(X, labels)

msg = ["win free lottery now"]

x = tfidf.transform(msg)

print("KNN:", "Spam" if knn.predict(x)[0] else "Not Spam")
print("SVM:", "Spam" if svc.predict(x)[0] else "Not Spam")
