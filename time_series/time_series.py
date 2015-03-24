import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

# load the 2014 lending club statistics
df = pd.read_csv('/home/dwhitena/Documents/Thinkful/Unit_2/multivariate/LoanStats3c.csv', \
	header=1, low_memory=False)
df = df.dropna(subset=['issue_d'])

# set the dataframe index as monthly periods
index = pd.PeriodIndex(df.issue_d, freq='M')
df = df.set_index(index)

# group by to get the time series
issuedts = df['issue_d'].groupby(df.index).count()

# plot the issued loans time series
plt.figure()
issuedts.plot()
plt.ylabel('Issued Loans')
plt.draw()
plt.savefig('time_series_plot.png')

# plot the ACF
plt.figure()
sm.graphics.tsa.plot_acf(issuedts)
plt.draw()
plt.savefig('acf_plot.png')

# plot the PACF
plt.figure()
sm.graphics.tsa.plot_pacf(issuedts)
plt.draw()
plt.savefig('pacf_plot.png')

# show all plots
plt.show()

# print conclusions
print "There seem to be some minor seasonality, but more data points may help confirm trends."