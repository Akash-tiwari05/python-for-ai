#Mean squared Error()

import numpy as np


#mse = 1/n*sum((y_i - y_pred_i)**2)

y_act = np.array([2.5,3.5,4.5,5.5])
y_pred = np.array([3.0,3.7,4.0,5.0])


mse = np.mean((y_act - y_pred)**2)
print("MSE: ",mse)


#Mean absolute error

#mae = 1/n sum (|y_act - y_pred|)

mae = np.mean(np.abs(y_act - y_pred))
print("MEA: ",mae)


#Root Mean Squred Error
#smse = (1/n*sum((y_i - y_pred_i)**2))^1/2

smse = np.sqrt(mse)
print("SMSE: ",smse)