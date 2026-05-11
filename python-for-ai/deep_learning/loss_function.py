import numpy as np

#Classifaction of Loss Function

#Binary Cross Entropy
#Loss = -[ylog(y_pred)+(1-y)*log(1-y_pred)]


y = 1
y_pre = 0.95

bse = -(y * np.log(y_pre) +(1 - y) * np.log(1 - y_pre))
print("Binary Cross Entropy Loss: ", bse)


#Categorical Entropy Loss
#Loss = - sum(ylog(y_pred))

# Actual binary labels
y_act = np.array([1, 0, 1, 1])

# Predicted probabilities
y_pred = np.array([0.9, 0.2, 0.8, 0.7])

# CSE Loss
loss = -np.mean(y_act*np.log(y_pred))

print("Categorical Entropy Loss:", loss)
print("Mean CSE Loss:", np.mean(loss))