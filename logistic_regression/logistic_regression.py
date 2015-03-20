import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import sys

# ---------------
# LOAD AND PREPARE DATA
# ---------------

# load cleaned data
df = pd.read_csv('loansData_clean.csv')

# Add column indicating if Interest rate is < 12%
df['Interest.Above.Threshold'] = df['Interest.Rate'].map(lambda num: num < 0.12)

# Add intercept column
df['Intercept'] = 1

# create a list of independent variables (including intercept)
ind_vars = ['FICO.Score', 'Amount.Requested', 'Intercept']


# ---------------
# LOGISTIC REGRESSION MODEL
# ---------------

# Define the model
logit = sm.Logit(df['Interest.Above.Threshold'], df[ind_vars])

# Fit the model
f = logit.fit()
coeff = f.params


# ---------------
# LOGISTIC FUNCTION AND PREDICTION
# ---------------

# get user defined fico and loan amount
print(' ')
fscore = int(raw_input('Enter a FICO score: '))
print(' ')
lamount = int(raw_input('Enter a loan amount: '))
print(' ')

# Define function that produces p for a FICO score 
# and loan Amount
def logistic_function(fscore,lamount,coeff):
	p = 1/(1 + np.exp(-(coeff[2] + coeff[0]*fscore + coeff[1]*lamount)))
	return p

# define prediction function
def prediction(fscore, lamount, coeff):
	p = logistic_function(fscore, lamount, coeff)
	if p >= 0.70:
		print('Yep, you will get the loan!')
	else:
		print('Sorry, pay off your current loans before getting more.')

# execute prediction function
prediction(fscore, lamount, coeff)

# visualize logistic function for loan amount $10000
#x = np.arange(550,950,1)
#y = 1/(1 + np.exp(-coeff[2] - coeff[0]*x - coeff[1]*10000))
#plt.figure()
#plt.plot(x,y)
#plt.draw()
#plt.savefig('logistic_function.png')
