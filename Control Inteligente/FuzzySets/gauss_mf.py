import numpy as np
import skfuzzy as sk
from matplotlib import pyplot as plt
#Defining the Numpy array for Tip Quality
x_qual = np.arange(0, 10.1, 0.1)
#Defining the Numpy array for Triangular membership functions
qual_lo = sk.gaussmf(x_qual, 0, 1)
qual_me = sk.gaussmf(x_qual, np.mean(x_qual), 1)
qual_hi = sk.gaussmf(x_qual, 10, 1)
#print(x_qual)
#print(qual_lo)
plt.plot(x_qual,qual_lo)
plt.plot(x_qual,qual_me)
plt.plot(x_qual,qual_hi)
plt.show()