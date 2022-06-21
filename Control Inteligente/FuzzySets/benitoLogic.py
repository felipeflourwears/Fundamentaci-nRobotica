from re import M
import numpy as np
import skfuzzy as sk
from matplotlib import pyplot as plt


x = 60
y = 60

# velocidad peaton 
x_qual = np.arange(2.01, 10.01, 0.01)

# intervalos peatones
turtleSpeed = sk.sigmf(x_qual, 2.5, -3.5)
lowSpeed = sk.trapmf(x_qual, [3, 4, 5, 6])
mediumSpeed = sk.trapmf(x_qual, [5.5, 6.5, 7, 7.5])
highSpeed = sk.trapmf(x_qual, [7.4, 8.0, 8.7, 9.2])
mcqueenLightningSpeed = sk.sigmf(x_qual, 9.5, 7.1) # algumentos -> media numerica y la desviación estandar 



# velocidad auto
velAuto = np.arange(0, 120)
#Defining the Numpy array for Triangular membership functions
vb = sk.trimf(velAuto, [0, 0, 40])
vm = sk.trimf(velAuto, [30, 60, 100])
va = sk.trimf(velAuto, [80, 120, 120])

# distancia coche
dist = np.arange(5,120)
dc = sk.trapmf(dist, [5, 5, 20, 35])
dm = sk.trapmf(dist, [20, 45, 60, 80])
dl = sk.trapmf(dist, [60, 80, 120, 120])



# Minimos
R1 = min(vb[x], dc[y])
R2 = min(vb[x], dm[y])
R3 = min(vb[x], dl[y])
R4 = min(vm[x], dc[y])
R5 = min(vm[x], dm[y])
R6 = min(vm[x], dl[y])
R7 = min(va[x], dc[y])
R8 = min(va[x], dm[y])
R9 = min(va[x], dl[y])

# MAximos
max_b = R3
max_mb = max(R2, R6)
max_m = max(R1, R5, R9)
max_ma = max(R4, R8)
max_a = R7


# CORTES p
b = turtleSpeed.copy()
mb = lowSpeed.copy()
m = mediumSpeed.copy()
ma = highSpeed.copy()
a = mcqueenLightningSpeed.copy()



b[b > max_b] = max_b
mb[mb > max_mb] = max_mb
m[m > max_m] = max_m
ma[ma > max_ma] = max_ma
a[a > max_a] = max_a

arr = list()
for i in range(len(b)):
    arr.append(max(b[i],mb[i],m[i],ma[i],a[i]))

muuu1 = 0.0
muuu2 = 0.0
for i in range(len(arr)):
    muuu1 += arr[i] * (i * (10/len(arr)))
    muuu2 += arr[i]

zzzzz = muuu1 / muuu2

print("mu1: ", muuu1)
print("mu2: ", muuu2)
print("zzz: ", zzzzz)

plt.figure()

plt.subplot(2,2,1)
#velocidad auto
plt.title("velocidad auto")
plt.plot(velAuto,vb)
plt.plot(velAuto,vm)
plt.plot(velAuto,va)
plt.legend(["Baja","Media","Alta"])

plt.subplot(2,2,2)
# distancia auto
plt.title("distancia auto")
plt.plot(dist,dc)
plt.plot(dist,dm)
plt.plot(dist,dl)
plt.legend(["Baja","Media","Alta"])



plt.subplot(2,2,3)
# valocidad peaton
plt.title("velocidad peaton")
plt.plot(x_qual,turtleSpeed)
plt.plot(x_qual,lowSpeed)
plt.plot(x_qual,mediumSpeed)
plt.plot(x_qual,highSpeed)
plt.plot(x_qual,mcqueenLightningSpeed)
plt.legend(["Tortuga","Baja","Media","Alta","RayoMcQueen"])


plt.subplot(2,2,4)
plt.title("velocidad final")
plt.plot(x_qual,arr)
ax = plt.gca()
ax.set_ylim([0,1])
#plt.plot(x_qual,mb)
#plt.plot(x_qual,m)
#plt.plot(x_qual,ma)
#plt.plot(x_qual,a)
#plt.legend(["Tortuga","Baja","Media","Alta","RayoMcQueen"])
plt.show()