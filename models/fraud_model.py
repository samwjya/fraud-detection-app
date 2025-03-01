import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt 
import seaborn as sns


df = pd.read_csv("../data/processed_creditcard.csv")

#X and Y axis. We drop Class because we use Class for predicting instead of training
X = df.drop("Class", axis = 1)
y = df["Class"]

# Split into 80% training and 20% testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

print("Training set size: ", X_train.shape)
print("Testing set size: ", X_test.shape)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(max_iter = 2000, solver='lbfgs')
model.fit(X_train, y_train)

y_prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, y_prediction)
print(f"Accuracy: {accuracy:.4f}")

