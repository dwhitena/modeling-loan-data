import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm


# load in data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


# ---------------
# CLEAN DATA
# ---------------

# lambda functions:
# strip percent signs
stripsign = lambda element: round(float(element.rstrip('%'))/100, 4)
# strip month
stripmonth = lambda element: int(element.rstrip(' months'))
# convert to string and split on '-'
splitfico = lambda element: str(element).split('-')
# convert pairs of FICO scores to int, pick min
convfico = lambda element: min([int(num) for num in element])

# strip percent signs from interest rate data
loansData['Interest.Rate'] = map(stripsign, loansData['Interest.Rate'])

# strip month from loan length
loansData['Loan.Length'] = map(stripmonth, loansData['Loan.Length'])

# format FICO scores
loansData['FICO.Score'] = map(splitfico, loansData['FICO.Range'])
loansData['FICO.Score'] = map(convfico, loansData['FICO.Score'])

#print loansData['Interest.Rate'][0:5]
#print loansData['Loan.Length'][0:5]
#print loansData['FICO.Score'][0:5]

# export clean loans data
loansData.to_csv('loansData_clean.csv', header=True, index=False)


# ---------------
# Print and Save Histogram
# ---------------
plt.figure()
p = loansData['FICO.Score'].hist()
plt.draw()
plt.savefig('fico_histogram.png')


# ---------------
# Generate Scatterplot Matrix
# ---------------
plt.figure()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.draw()
plt.savefig('loansdata_scatterplot_matrix.png')


# ---------------
# Linear Regression Model
# ---------------

# data
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# shape data
# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# form input matrix
x = np.column_stack([x1,x2])

# add column of ones (constant)
X = sm.add_constant(x)

# Ordinary Least Squares (OLS) model
model = sm.OLS(y,X)
f = model.fit()

# print model parameters
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

