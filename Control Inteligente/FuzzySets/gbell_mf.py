import numpy as np
import skfuzzy as sk
from matplotlib import pyplot as plt
#Defining the Numpy array for Tip Quality
x_qual = np.arange(0, 10.1, 0.1)
#Defining the Numpy array for Triangular membership functions
qual_lo = sk.gbellmf(x_qual, 1,2,0)
qual_me = sk.gbellmf(x_qual, 1,2,5)
qual_hi = sk.gbellmf(x_qual, 1,2,10)
#print(x_qual)
#print(qual_lo)
plt.plot(x_qual,qual_lo)
plt.plot(x_qual,qual_me)
plt.plot(x_qual,qual_hi)
plt.show()