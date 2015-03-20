import collections
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import os

# clear any previously paved plots
os.system("rm *.png")


# --------------
# FREQUENCIES
# --------------

# data
testlist = [1, 4, 5, 6, 9, 9, 9]

# calculate counts
c = collections.Counter(testlist)

# total number of instances
count_sum = sum(c.values())

# calculate and print frequencies
for k,v in c.iteritems():
	print "The frequency of " + str(k) + " is " + str(float(v)/count_sum)


# --------------
# BASIC BOX PLOT
# --------------

# data
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

# generate and save boxplot
plt.figure()
plt.boxplot(x)
plt.draw()
plt.savefig("boxplot.png")


# --------------
# HISTOGRAM
# --------------

# generate and save histogram
plt.figure()
plt.hist(x, histtype='bar')
plt.draw()
plt.savefig("histogram.png")


# --------------
# QQ-Plots
# --------------

# generate and save QQ-plot of normal data
plt.figure()
test_data = np.random.normal(size=1000)   
stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("normal_qq_plot.png")

# generate and save QQ-plot of uniform data
plt.figure()
test_data2 = np.random.uniform(size=1000)   
stats.probplot(test_data2, dist="norm", plot=plt)
plt.savefig("uniform_qq_plot.png")


# show all plots
plt.show()