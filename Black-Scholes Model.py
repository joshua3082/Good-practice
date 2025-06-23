#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
from scipy.stats import norm

def Black_Scholes(S, T, X, r, sigma, option):
    # S As current market price of asset
    # X is the exercise price of the option
    # R is the risk free interest rate
    # T is the time to expiration of the option
    # sigma is standard deviation of volatility of the asset
    d1 = np.log(S/X) + ((r + (sigma**2)/2))*T
    d1 = d1 / (sigma*np.sqrt(T))
    d2 = d1 - (sigma*np.sqrt(T))
    
    while option != "call" and option != "put":
        option = input("Please enter call or put ")
    if option == "call":
        C = S * norm.cdf(d1) - X*np.exp(-r*T) * norm.cdf(d2)
    elif option == "put":
        C =  X*np.exp(-r*T) * norm.cdf(-d2) - (S * norm.cdf(-d1))
    return(C)

def Greeks_call(S, T, X, r, sigma):
    d1 = np.log(S/X) + ((r + (sigma**2)/2))*T
    d1 = d1 / (sigma*np.sqrt(T))
    d2 = d1 - (sigma*np.sqrt(T))
    N_prime = norm.pdf(d1)
    delta = norm.cdf(d1)
    delta = round(delta, 3)#Because delta is the rate of change of the option price which is dC/dS
    gamma = N_prime / (S *sigma * np.sqrt(T))
    gamma = round(gamma, 5)
    vega = S * np.sqrt(T) * N_prime
    vega = round(vega, 3)
    theta = -(S * sigma * N_prime)/ (2 * np.sqrt(T)) - r * X * np.exp(-r*T)*norm.cdf(d2)
    theta = round(theta, 3)
    rho = X * T * np.exp(-r*T) * norm.cdf(d2)
    rho = round(rho, 3)
    return{"delta": delta, "gamma": gamma, "vega": vega, "theta": theta, "rho": rho}

def Greeks_put(S, T, X, r, sigma):
    d1 = np.log(S/X) + ((r + (sigma**2)/2))*T
    d1 = d1 / (sigma*np.sqrt(T))
    d2 = d1 - (sigma*np.sqrt(T))
    N_prime = norm.pdf(d1)
    delta = norm.cdf(d1) - 1 #Because delta is the rate of change of the option price which is dC/dS
    delta = round(delta, 3)
    gamma = N_prime / (S *sigma * np.sqrt(T))
    gamma = round(gamma, 5) #Rounded gamma to 5 d.p because often is quite small
    vega = S * np.sqrt(T) * N_prime
    vega = round(vega, 3)
    theta = -(S * sigma * N_prime)/ (2 * np.sqrt(T)) + r * X * np.exp(-r*T)*norm.cdf(-d2)
    theta = round(theta, 3)
    rho = -X * T * np.exp(-r*T) * norm.cdf(-d2)
    rho = round(rho, 3)
    return{"delta": delta, "gamma": gamma, "vega": vega, "theta": theta, "rho": rho}

print(Black_Scholes(100, 3, 60, 0.2, 0.3, "call"))
print(Greeks_call(100, 3, 60, 0.2, 0.3))


# In[ ]:




