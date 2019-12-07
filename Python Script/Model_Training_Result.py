#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error 


# In[2]:


df = pd.read_csv('segment16.csv')
#df.head(10)


# In[3]:


# Extract the training and test data
data = df.values
X = data[:,[4,6]]
y = data[:,3]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=12)
#X_train[:10]


# In[4]:


# Scale the data to be between 0 and 1
#scaler = StandardScaler()
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
#X_train[:10]


# In[5]:


# Establish a SVR model with parameters
model = SVR(C=1, cache_size=500, epsilon=0.1, kernel='rbf', gamma='auto')
#model = SVR(C=100, cache_size=500, epsilon=4, kernel='rbf', gamma='auto')


# In[6]:


# Train the model
model.fit(X_train, y_train)


# In[7]:


#Final RMSE of the model
pred_y = model.predict(X_test)

mse =mean_squared_error(y_test, pred_y)
print("Mean Squared Error:",mse)
 
rmse = math.sqrt(mse)
print("Root Mean Squared Error:", rmse)


# In[8]:


# Try to get the lowest RMSE by using different Epsilon value
epsilons = np.arange(1,25)
scores = []
for e in epsilons:
    model.set_params(epsilon=e)
    model.fit(X_train, y_train)
    scores.append(math.sqrt(mean_squared_error(y_test, model.predict(X_test))))
plt.plot(epsilons, scores)
plt.title("Epsilon effect")
plt.xlabel("epsilon")
plt.ylabel("RMSE")
plt.show()


# In[9]:


# Try to get the lowest RMSE by using different C value with Epsilon value above, then retrain the model again above
model.set_params(epsilon=2)
Cs = np.arange(1,200)
scores = []
for c in Cs:
    model.set_params(C=c)
    model.fit(X_train, y_train)
    scores.append(math.sqrt(mean_squared_error(y_test, model.predict(X_test))))
plt.plot(Cs, scores)
plt.title("C effect")
plt.xlabel("C")
plt.ylabel("RMSE")
plt.show()


# In[ ]:




