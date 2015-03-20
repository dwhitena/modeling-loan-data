import pandas as pd
import scipy.stats as stats
import collections
import matplotlib.pyplot as plt


# read in data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# clean data
loansData.dropna(inplace=True)

# count frequencies of open credit lines
freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# visualize the data
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.draw()
plt.savefig("bar_plot_lending.png")

# compute chi-squared
chi, p = stats.chisquare(freq.values())

# print the result
print "Chi-squared for the Open Credit Line data is " + str(chi)

# show all plots
plt.show()