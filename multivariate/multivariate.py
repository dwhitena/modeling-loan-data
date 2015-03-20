import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf


# load the 2014 lending club statistics
df = pd.read_csv('LoanStats3c.csv', skiprows=1)


# ---------------
# CLEAN DATA
# ---------------

# remove null values and "NaN"
df = df[['int_rate','annual_inc','home_ownership']]
df.dropna(inplace=True)
df = df[df.int_rate != 'NaN']

# strip percent signs in int_rate and covert to float
df['int_rate'] = df['int_rate'].map(lambda \
	element: round(float(element.rstrip('%'))/100, 4))

# convert incomes to integers
df['annual_inc'] = df['annual_inc'].map(lambda element: int(element))


# -------------------------------
# MODEL INTEREST RATE VS. INCOME
# -------------------------------

# variables
intrate = df['int_rate']
annualincome = df['annual_inc']

# shape data
# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x = np.matrix(annualincome).transpose()

# add column of ones (constant)
X = sm.add_constant(x)

# Linear model
model1 = sm.OLS(y,X).fit()
print 'Income Coefficient: ', model1.params[1]
print 'Intercept: ', model1.params[0]
print 'P-Values: ', model1.pvalues  # ??? why do these come out zero ???
print 'R-Squared: ', model1.rsquared

# NOTE: this does not appear to model the data very well.  The intercept, is
# basically the mean of the interest rates, and the r-squared indicates that
# the model does not fit the data very well. The coefficient of the annual 
# income is so small, it seems negligible.
# To visualize this see the following plot:
plt.figure()
plt.scatter(df['annual_inc'], \
	df['int_rate'], alpha=0.3)
plt.xlabel('Annual Income')
plt.ylabel('Interest Rate')
plt.draw()
plt.savefig('rate_vs_income.png')


# -------------------------------------------------
# MODEL INTEREST RATE VS. INCOME AND HOME OWNERSHIP
# -------------------------------------------------
# (no interactions)

# encode df.home_ownership as a numeric via pd.Categorical
df['home_dummy'] = pd.Categorical(df.home_ownership).labels

# Multiple regression model
model2 = smf.ols(formula="int_rate ~ home_dummy + annual_inc", data=df).fit()
print model2.summary()


# -------------------------------------------------
# MODEL INTEREST RATE VS. INCOME AND HOME OWNERSHIP
# -------------------------------------------------
# (with interactions)

# encode df.home_ownership as a numeric via pd.Categorical
df['home_dummy'] = pd.Categorical(df.home_ownership).labels

# Multiple regression model
model3 = smf.ols(formula="int_rate ~ home_dummy*annual_inc", data=df).fit()
print model3.summary()
