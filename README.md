This repository just includes some projects that I thought would interesting as a start in GitHub.

The main project here is the Black_Scholes calculator.

Features
- Calculates European option price for both call and put options
- Computes all Greeks 
- Uses NumPy and SciPy for mathematical and statistical operations

Potential improvements are graphs for visualisation of the Greeks and their importance and maybe adding a subsection for other pricing models to compare against it

To use the model:
Run the `Black_Scholes.py`
from Black_Scholes import Black_Scholes, Greeks_call, Greeks_put
print(Black_Scholes(100, 3, 60, 0.2, 0.3, 'call')) which should output 67.24
The last argument can be changed to 'put' to output a put option but remember to change the other variables accordingly.
Any other values other than "put" or "call" will prompt the user to enter one of these which will carry on indefinitiely until they do

I've split the Greeks into two separate function for Greek Calls and Greek puts just becuase it was a lot more formulas than the Black_Scholes function
This means there is only 5 arguments for the Greek function and NOT 6 unlike the Black_Scholes.
print(Greeks_call(100, 3, 60, 0.2, 0.3)) Should output the values {'delta': 0.992, 'gamma': 0.00043, 'vega': 3.901, 'theta': -6.582, 'rho': 95.804} All to 3d.p
