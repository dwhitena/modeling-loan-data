import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import os

# clear any previously saved plots
os.system("rm *.png")


# read in data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# clean data
loansData.dropna(inplace=True)

# generate and save box plot
plt.figure()
loansData.boxplot(column='Amount.Requested')
plt.draw()
plt.savefig("boxplot_lending.png")

# generate and save histogram
plt.figure()
loansData.hist(column='Amount.Requested')
plt.draw()
plt.savefig("histogram_lending.png")

# visually test to see if data follows normal dist
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.draw()
plt.savefig("qq_lending.png")


# show all plots
plt.show()