import numpy as np 
import pandas as pd 
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("creditcard_2023.csv")


scaler = StandardScaler()
df["Amount"] = scaler.fit_transform(df["Amount"].values.reshape(-1,1))

df.to_csv("processed_creditcard.csv", index=False)
print("Processed dataset saved!")