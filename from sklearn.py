from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset and split
X, Y = load_iris(return_X_y=True)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1/3, random_state=42)

# Train model and make predictions
model = GaussianNB().fit(X_train, Y_train)
predictions = model.predict(X_test)

# Evaluate
print("\nPredictions:", predictions)
print("Actual:", Y_test)
print("Accuracy:", accuracy_score(Y_test, predictions))
print("Confusion Matrix:\n", confusion_matrix(Y_test, predictions))