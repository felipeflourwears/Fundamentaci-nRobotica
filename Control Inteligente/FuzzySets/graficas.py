import numpy as np
import csv
import skfuzzy as sk
from matplotlib import pyplot as plt

"""
x_qual=np.arange(-180, 180, 1)
turtleSpeed = sk.gbellmf(x_qual, 45, 2, -180)
lowSpeed = sk.gbellmf(x_qual, 45, 2, -90)
mediumSpeed = sk.gbellmf(x_qual, 45, 2, 0)
highSpeed = sk.gbellmf(x_qual, 45, 2, 90)
mcqueenLightningSpeed =sk.gbellmf(x_qual, 45, 2, 180)

plt.figure()
# valocidad peaton
plt.title("Desviación Eje X")
plt.plot(x_qual,turtleSpeed)
plt.plot(x_qual,lowSpeed)
plt.plot(x_qual,mediumSpeed)
plt.plot(x_qual,highSpeed)
plt.plot(x_qual,mcqueenLightningSpeed)
plt.legend(["Desvb","DesvMedbaja","DesvMedia","DesvMediaAlta","DesvAlto"])
plt.show()
"""

"""
x_qual = np.arange(0.0, 16.0, 0.1)
distBaja = sk.gbellmf(x_qual, 2, 2, 0.0)
distBajaMedia = sk.gbellmf(x_qual, 2, 2, 4.0)
distMedia = sk.gbellmf(x_qual, 2, 2, 8.0)
distMediaAlta = sk.gbellmf(x_qual, 2, 2, 12.0)
distAlta= sk.gbellmf(x_qual, 2, 2, 16.0)

plt.figure()
# valocidad peaton
plt.title("Distancia entre Tortugas")
plt.plot(x_qual,distBaja)
plt.plot(x_qual,distBajaMedia)
plt.plot(x_qual,distMedia)
plt.plot(x_qual,distMediaAlta)
plt.plot(x_qual,distAlta)
plt.legend(["distBaja","distMedioBaja","distMedia","distMediaAlta","distAlto"])
plt.show()
"""
"""
x_qual = np.arange(0, 4, 0.1)
baja = sk.trimf(x_qual, [0, 0, 1.0])
mediabaja = sk.trimf(x_qual, [0, 1.0, 2.0])
media = sk.trimf(x_qual, [1.0, 2.0, 3.0])
mediaAlta = sk.trimf(x_qual, [2.0, 3.0, 4.0])
Alta = sk.trimf(x_qual, [3.0, 4.0, 4.0])

plt.figure()
# valocidad peaton
plt.title("Velocidad Lineal")
plt.plot(x_qual,baja)
plt.plot(x_qual,mediabaja)
plt.plot(x_qual,media)
plt.plot(x_qual,mediaAlta)
plt.plot(x_qual,Alta)
plt.legend(["VelBaja","VelMedioBaja","VelMedia","VelMediaAlta","VelAlto"])
plt.show()
"""

x_qual = np.arange(-2, 2, 0.1)
baja = sk.trimf(x_qual, [-2.0, -2.0, -1.0])
mediabaja = sk.trimf(x_qual, [-2.0, -1.0, 0])
media = sk.trimf(x_qual, [-1.0, 0, 1.0])
mediaAlta = sk.trimf(x_qual, [0, 1.0, 2.0])
Alta = sk.trimf(x_qual, [1.0, 2.0, 2.0])

plt.figure()
# valocidad peaton
plt.title("Velocidad Angular")
plt.plot(x_qual,baja)
plt.plot(x_qual,mediabaja)
plt.plot(x_qual,media)
plt.plot(x_qual,mediaAlta)
plt.plot(x_qual,Alta)
plt.legend(["VelBaja","VelMedioBaja","VelMedia","VelMediaAlta","VelAlto"])
plt.show()