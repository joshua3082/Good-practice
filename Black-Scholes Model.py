#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.stats import norm

def Black_Scholes(S, T, X, r, d):
    # S As current market price of asset
    # X is the exercise price of the option
    # R is the risk free interest rate
    # T is the time to expiration of the option
    # d is standard deviation of volatility of the asset
    d1 = np.log(S/X) + ((r + (d**2)/2))*T
    d1 = d1 / (d*np.sqrt(T))
    d2 = d1 - (d*np.sqrt(T))
    
    C = S * norm.cdf(d1) - X*np.exp(-r*T) * norm.cdf(d2)
    return(C)

print(Black_Scholes(100,3,60, 0.2, 0.3))


# In[ ]:




