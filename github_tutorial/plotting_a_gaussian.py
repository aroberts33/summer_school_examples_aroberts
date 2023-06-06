from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

xvals = np.linspace(-30,30,60)
mean = 0.
std = 10.

plt.plot(xvals, norm.pdf(xvals, mean, std))
plt.show()
