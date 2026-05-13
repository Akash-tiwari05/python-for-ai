import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# load dataset
df = pd.read_csv(
    r"D:\PythonProjects\python-for-ai\deep_learning\iris.data.csv",
    header=None
)

df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

print(df.head())
print(df.isnull().sum())


X = df.iloc[:,0:4]
y = df["species"]


encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y.values.reshape(-1, 1))

#print(y_encoded)

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# neural network
model = MLPClassifier(
    hidden_layer_sizes=(10,),
    max_iter=1000,
    random_state=42
)

model.fit(X_train, y_train)

# predictions
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))