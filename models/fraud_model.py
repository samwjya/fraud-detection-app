import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
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



#-------------------------------------------------------------------------------------------------
# Logistice Regression (Accuracy: 99.83%)                                                        |                                                       
# scaler = StandardScaler()                                                                      |
# X_train = scaler.fit_transform(X_train)                                                        |
# X_test = scaler.transform(X_test)                                                              |
#                                                                                                |
# model = LogisticRegression(max_iter = 2000, solver='lbfgs')                                    |
# model.fit(X_train, y_train)                                                                    |
#-------------------------------------------------------------------------------------------------

# Random Forest()

model = RandomForestClassifier(n_estimators = 100, random_state = 42)
model.fit(X_train, y_train)


y_prediction = model.predict(X_test)

#Accuracy
accuracy = accuracy_score(y_test, y_prediction)
print(f"Accuracy: {accuracy:.4f}")

#Evaluate the model------------------------------------------------------------------------------
print("Classification report:\n", classification_report(y_test, y_prediction))

conf_matrix = confusion_matrix(y_test, y_prediction)

plt.figure(figsize=(6,4))
sns.heatmap(conf_matrix, annot = True, fmt = "d", cmap = "Blues", xticklabels = ["Not Fraud", "Fraud"], yticklabels = ["Not Fraud", "Fraud"] )
plt.xlabel("Predicted label")
plt.ylabel("True label")
plt.title("Confusion matrix")
plt.show()

#To save the model

import joblib

joblib.dump(model, "random_forest_model.pkl")
print("✅ Model saved successfully as models/random_forest_model.pkl")
