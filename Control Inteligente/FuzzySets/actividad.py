#Velocidades del carro y distancias del carro

#Primer gráfica

# Primer grafica
# Velocidad del carro   X=0-------100;20 km/m

# Segunda gráfica
# Distancia al auto      X=20-------80;20 m

#Tercera grafica         X=0-------12.5;2.5 km/h 
#Velocidad del peaton

#Cuarta gráfica agregado
import numpy as np
import skfuzzy as sk
from matplotlib import pyplot as plt
#Defining the Numpy array for Tip Quality
#Generar datos de 0 a 50

velAuto = np.arange(0, 120)
#Defining the Numpy array for Triangular membership functions
velAuto_baja = sk.trimf(velAuto, [0, 0, 40])
velAuto_media = sk.trimf(velAuto, [30, 60, 100])
velAuto_alta = sk.trimf(velAuto, [80, 120, 120])


plt.plot(velAuto,velAuto_baja)
#plt.plot(temp,temp_mediaBaja)
plt.plot(velAuto,velAuto_media)
#plt.plot(velAuto,temp_mediaAlta)
plt.plot(velAuto,velAuto_alta)
plt.show()

