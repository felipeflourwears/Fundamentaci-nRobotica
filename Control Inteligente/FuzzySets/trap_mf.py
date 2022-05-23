import numpy as np
import skfuzzy as sk
from matplotlib import pyplot as plt
#Defining the Numpy array for Tip Quality
x_qual = np.arange(0, 10.1, 0.1)
#Defining the Numpy array for Triangular membership functions
qual_lo = sk.trapmf(x_qual, [0, 0, 2 , 4])
qual_me = sk.trapmf(x_qual, [2, 4, 6, 8])
qual_hi = sk.trapmf(x_qual, [6, 8, 10, 10])
#print(x_qual)
#print(qual_lo)
plt.plot(x_qual,qual_lo)
plt.plot(x_qual,qual_me)
plt.plot(x_qual,qual_hi)
plt.show()