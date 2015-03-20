import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

# plot normal/Gaussian distribution
mean = 0
variance = 1
sigma = np.sqrt(variance) # this is the standard deviation
x = np.linspace(-3,3,100)
plt.plot(x, mlab.normpdf(x,mean,sigma))

plt.show()