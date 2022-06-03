import numpy as np
import skfuzzy as sk
from matplotlib import pyplot as plt


# velocidad peaton 
x_qual = np.arange(2.01, 8.01, 0.01)

# intervalos peatones
lS = sk.sigmf(x_qual, 2.5, -3.5) # algumentos -> media numerica y la desviación estandar 
lmS=sk.sigmf(x_qual, 6.9, 7.1) # algumentos -> media numerica y la desviación estandar 
mS = sk.trapmf(x_qual, [3, 4.5, 6, 7])
hmS = sk.trapmf(x_qual, [3, 4.5, 6.2, 7.3])
hS = sk.sigmf(x_qual, 2.5, -3.5)



# velocidad auto
velAuto = np.arange(0, 120)
#Defining the Numpy array for Triangular membership functions
velAuto_baja = sk.trimf(velAuto, [0, 0, 40])
velAuto_media = sk.trimf(velAuto, [30, 60, 100])
velAuto_alta = sk.trimf(velAuto, [80, 120, 120])

# distancia coche
dist = np.arange(5,120)
qual_lo = sk.trapmf(dist, [5, 5, 20, 35])
qual_me = sk.trapmf(dist, [20, 45, 60, 80])
qual_hi = sk.trapmf(dist, [60, 80, 120, 120])



plt.figure()
plt.subplot(1,3,1)
#velocidad auto
plt.title("velocidad auto")
plt.plot(velAuto,velAuto_baja)
plt.plot(velAuto,velAuto_media)
plt.plot(velAuto,velAuto_alta)
plt.legend(["Baja","Media","Alta"])


plt.subplot(1,3,2)
# distancia auto
plt.title("distancia auto")
plt.plot(dist,qual_lo)
plt.plot(dist,qual_me)
plt.plot(dist,qual_hi)
plt.legend(["Baja","Media","Alta"])

plt.subplot(1,3,3)
# valocidad peaton
plt.title("velocidad peaton")
plt.plot(x_qual,lS)
plt.plot(x_qual,lmS)
plt.plot(x_qual,mS)
plt.plot(x_qual,hmS)
plt.plot(x_qual,hS)
plt.legend(["Baja","Media","Alta"])


plt.show()