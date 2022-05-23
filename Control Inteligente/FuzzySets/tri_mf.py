import numpy as np
import skfuzzy as sk
from matplotlib import pyplot as plt
#Defining the Numpy array for Tip Quality
#Generar datos de 0 a 50
temp = np.arange(0, 51)
#Defining the Numpy array for Triangular membership functions
temp_baja = sk.trimf(temp, [0, 0, 12.5])
temp_mediaBaja= sk.trimf(temp, [0, 12.5, 25])
temp_media = sk.trimf(temp, [12.5, 25, 37.5])
temp_mediaAlta= sk.trimf(temp, [25, 37.5, 50])
temp_alta = sk.trimf(temp, [37.5, 50, 50])
#print(temp)
#print(qual_lo)


plt.plot(temp,temp_baja)
plt.plot(temp,temp_mediaBaja)
plt.plot(temp,temp_media)
plt.plot(temp,temp_mediaAlta)
plt.plot(temp,temp_alta)
plt.show()