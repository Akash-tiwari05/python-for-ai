import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


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

 #Split both features (X) and the encoded target (y_encoded)
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# neural network
model = Sequential([
    Dense(16, activation='relu', input_shape=(4,)),
    Dense(12, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model correctly and save the history
history = model.fit(
    X_train, 
    y_train, 
    epochs=50,          # Set number of training loops
    batch_size=8,       # Set batch size
    validation_data=(X_test, y_test) # Track test accuracy during training
)

loss, accuracy =model.evaluate(X_train,y_test)
print("Test Accuracy: ", accuracy)
print("Test loss: ",loss)
