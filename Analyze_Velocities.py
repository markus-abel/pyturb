# test d'analyse de donnees

import h5py
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats.stats


f = h5py.File('St0.99.h5', 'r')    # lecture du fichier

# il est important de connaitre la composition du fichier, les groupes qui le composent.

h = list(f)

print (h)

x = f['DNS']

x1 = list(x)

print(x1)

x2 = x['BEAM']

print (x2)

z = np.array(x2)

print ("Shape of z :", z.shape)


# Recuperation des donnees de vitesses pour toutes les particules:

tabTime = []

uX = np.zeros( (np.size(z[:,0]),np.size(z[0,:]) ))
uY = np.zeros( (np.size(z[:,0]),np.size(z[0,:]) ))
uZ = np.zeros( (np.size(z[:,0]),np.size(z[0,:]) ))

j = 0
while j < 3300 :

  i = 0
  while i < 1280:
  
    uX[j,i] = z[j][i][3]
    uY[j,i] = z[j][i][4]
    uZ[j,i] = z[j][i][5]
  
    i = i + 1

  j = j + 1
  
  tabTime.append(j)


# Analyse des vitesses :

"""
Standard deviation and Moments of velocities :

"""

StduX = np.zeros( (np.size(z[:,0]), 1) )
StduY = np.zeros( (np.size(z[:,0]), 1) )
StduZ = np.zeros( (np.size(z[:,0]), 1) )

Moment2ux = np.zeros( (np.size(z[:,0]), 1) )
Moment2uy = np.zeros( (np.size(z[:,0]), 1) )
Moment2uz = np.zeros( (np.size(z[:,0]), 1) )

Moment4ux = np.zeros( (np.size(z[:,0]), 1) )
Moment4uy = np.zeros( (np.size(z[:,0]), 1) )
Moment4uz = np.zeros( (np.size(z[:,0]), 1) )

Moment6ux = np.zeros( (np.size(z[:,0]), 1) )
Moment6uy = np.zeros( (np.size(z[:,0]), 1) )
Moment6uz = np.zeros( (np.size(z[:,0]), 1) )

M2xStduX = np.zeros( (np.size(z[:,0]), 1) )
M2yStduY = np.zeros( (np.size(z[:,0]), 1) )
M2zStduZ = np.zeros( (np.size(z[:,0]), 1) )

M4xStduX = np.zeros( (np.size(z[:,0]), 1) )
M4yStduY = np.zeros( (np.size(z[:,0]), 1) )
M4zStduZ = np.zeros( (np.size(z[:,0]), 1) )

M6xStduX = np.zeros( (np.size(z[:,0]), 1) )
M6yStduY = np.zeros( (np.size(z[:,0]), 1) )
M6zStduZ = np.zeros( (np.size(z[:,0]), 1) )

m = 0 
while m < 3300 :

  StduX[m] = scipy.std(uX[m])
  StduY[m] = scipy.std(uY[m])
  StduZ[m] = scipy.std(uZ[m])

  Moment2ux[m] = scipy.stats.moment(uX[m], moment=2)  
  Moment2uy[m] = scipy.stats.moment(uY[m], moment=2)
  Moment2uz[m] = scipy.stats.moment(uZ[m], moment=2)

  Moment4ux[m] = scipy.stats.moment(uX[m], moment=4)  
  Moment4uy[m] = scipy.stats.moment(uY[m], moment=4)
  Moment4uz[m] = scipy.stats.moment(uZ[m], moment=4)

  Moment6ux[m] = scipy.stats.moment(uX[m], moment=6)  
  Moment6uy[m] = scipy.stats.moment(uY[m], moment=6)
  Moment6uz[m] = scipy.stats.moment(uZ[m], moment=6)

  M2xStduX[m] = np.divide(Moment2ux[m], StduX[m])
  M2yStduY[m] = np.divide(Moment2uy[m], StduY[m])
  M2zStduZ[m] = np.divide(Moment2uz[m], StduZ[m])

  M4xStduX[m] = np.divide(Moment4ux[m], (np.power(StduX[m], 2)) )
  M4yStduY[m] = np.divide(Moment4uy[m], (np.power(StduY[m], 2)) )
  M4zStduZ[m] = np.divide(Moment4uz[m], (np.power(StduZ[m], 2)) )

  M6xStduX[m] = np.divide(Moment6ux[m], (np.power(StduX[m], 3)) )
  M6yStduY[m] = np.divide(Moment6uy[m], (np.power(StduY[m], 3)) )
  M6zStduZ[m] = np.divide(Moment6uz[m], (np.power(StduZ[m], 3)) )

  m = m + 1


"""
Tous les plots a 1D :

"""


# Plot 1D de la variance :

plt.figure(1)

plt.title("Standard deviation of uX, uY, uZ of 1280 particles for 3300 dt and St = 0.99")
plt.xlabel("Time")
plt.ylabel("Standard deviation")
plt.plot(tabTime, StduX)
plt.plot(tabTime, StduY)
plt.plot(tabTime, StduZ)
plt.legend(("Standard deviation of uX", "Standard deviation of uY", "Standard deviation of uZ"), 'best') 

# Plot 1D des moments 2:

plt.figure(2)

plt.title("Moments 2 of uX, uY, uZ of 1280 particles for 3300 dt and St = 0.99")
plt.xlabel("Time")
plt.ylabel("Moment 2")
plt.plot(tabTime, Moment2ux)
plt.plot(tabTime, Moment2uy)
plt.plot(tabTime, Moment2uz)
plt.legend(("Moment 2 of uX", "Moment 2 of uY", "Moment 2 of uZ"), 'best') 

# Plot 1D des moments 4:

plt.figure(3)

plt.title("Moments 4 of uX, uY, uZ of 1280 particles for 3300 dt and St = 0.99")
plt.xlabel("Time")
plt.ylabel("Moment 4")
plt.plot(tabTime, Moment4ux)
plt.plot(tabTime, Moment4uy)
plt.plot(tabTime, Moment4uz)
plt.legend(("Moment 4 of uX", "Moment 4 of uY", "Moment 4 of uZ"), 'best') 

# Plot 1D des moments 6:

plt.figure(4)

plt.title("Moments 6 of uX, uY, uZ of 1280 particles for 3300 dt and St = 0.99")
plt.xlabel("Time")
plt.ylabel("Moment 6")
plt.plot(tabTime, Moment6ux)
plt.plot(tabTime, Moment6uy)
plt.plot(tabTime, Moment6uz)
plt.legend(("Moment 6 of uX", "Moment 6 of uY", "Moment 6 of uZ"), 'best') 

# Plot 1D du rapport des moments 2 sur la variance :

plt.figure(5)

plt.title("Moments 2 of uX, uY, uZ on Standard deviation of uX, uY, uZ of 1280 particles for 3300 dt and St = 0.99")
plt.xlabel("Time")
plt.ylabel("Moment 2 / Standard deviation")
plt.plot(tabTime, M2xStduX)
plt.plot(tabTime, M2yStduY)
plt.plot(tabTime, M2zStduZ)
plt.legend(("Moment 2 / Standard deviation of uX", "Moment 2 / Standard deviation of uY", "Moment 2 / Standard deviation of uZ"), 'best') 

# Plot 1D du rapport des moments 4 sur la variance au carre :

plt.figure(6)

plt.title("Moments 4 of uX, uY, uZ on (Standard deviation)2 of uX, uY, uZ of 1280 particles for 3300 dt and St = 0.99")
plt.xlabel("Time")
plt.ylabel("Moment 4 / (Standard deviation)2")
plt.plot(tabTime, M4xStduX)
plt.plot(tabTime, M4yStduY)
plt.plot(tabTime, M4zStduZ)
plt.legend(("Moment 4 / (Standard deviation)2 of uX", "Moment 4 / (Standard deviation)2 of uY", "Moment 4 / (Standard deviation)2 of uZ"), 'best') 

# Plot 1D du rapport des moments 6 sur la variance au cube :

plt.figure(7)

plt.title("Moments 6 of uX, uY, uZ on (Standard deviation)3 of uX, uY, uZ of 1280 particles for 3300 dt and St = 0.99")
plt.xlabel("Time")
plt.ylabel("Moment 6 / (Standard deviation)3")
plt.plot(tabTime, M6xStduX)
plt.plot(tabTime, M6yStduY)
plt.plot(tabTime, M6zStduZ)
plt.legend(("Moment 6 / (Standard deviation)3 of uX", "Moment 6 / (Standard deviation)3 of uY", "Moment 6 / (Standard deviation)3 of uZ"), 'best') 

"""
Tous les plots 3D :

"""

# Plot 3D de la variance :

fig = plt.figure(8)
  
ax = fig.gca(projection='3d')

ax.set_title("Standard deviation of 1280 particles for 3300 dt and St = 0.99")
ax.set_xlabel('Standard deviation of uX')
ax.set_ylabel('Standard deviation of uY')
ax.set_zlabel('Standard deviation of uZ')

ax.plot(np.concatenate(StduX), np.concatenate(StduY), np.concatenate(StduZ), label='Standrad deviation 3D')

# Plot 3D des moments 2:

fig = plt.figure(9)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 2 of 1280 particles for 3300 dt and St = 0.99")
ax.set_xlabel('Moment 2 of uX')
ax.set_ylabel('Moment 2 of uY')
ax.set_zlabel('Moment 2 of uZ')

ax.plot(np.concatenate(Moment2ux), np.concatenate(Moment2uy), np.concatenate(Moment2uz), label='Moment 2 3D')

# Plot 3D des moments 4:

fig = plt.figure(10)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 4 of 1280 particles for 3300 dt and St = 0.99")
ax.set_xlabel('Moment 4 of uX')
ax.set_ylabel('Moment 4 of uY')
ax.set_zlabel('Moment 4 of uZ')

ax.plot(np.concatenate(Moment4ux), np.concatenate(Moment4uy), np.concatenate(Moment4uz), label='Moment 4 3D')

# Plot 3D des moments 6:

fig = plt.figure(11)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 6 of 1280 particles for 3300 dt and St = 0.99")
ax.set_xlabel('Moment 6 of uX')
ax.set_ylabel('Moment 6 of uY')
ax.set_zlabel('Moment 6 of uZ')

ax.plot(np.concatenate(Moment6ux), np.concatenate(Moment6uy), np.concatenate(Moment6uz), label='Moment 6 3D')

# Plot 3D du rapport des moments 2 sur la variance :

fig = plt.figure(12)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 2 of uX, uY, uZ on Standard deviation of uX, uY, uZ of 1280 particles for 3300 dt and St = 0.99")
ax.set_xlabel('Moment 2 / Standard deviation of uX')
ax.set_ylabel('Moment 2 / Standard deviation of uY')
ax.set_zlabel('Moment 2 / Standard deviation of uZ')

ax.plot(np.concatenate(M2xStduX), np.concatenate(M2yStduY), np.concatenate(M2zStduZ), label='Moment 2 / Standard deviation 3D')

# Plot 3D du rapport des moments 4 sur la variance au carre :

fig = plt.figure(13)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 4 of uX, uY, uZ on (Standard deviation)2 of uX, uY, uZ of 1280 particles for 3300 dt and St = 0.99")
ax.set_xlabel('Moment 4 / (Standard deviation)2 of uX')
ax.set_ylabel('Moment 4 / (Standard deviation)2 of uY')
ax.set_zlabel('Moment 4 / (Standard deviation)2 of uZ')

ax.plot(np.concatenate(M4xStduX), np.concatenate(M4yStduY), np.concatenate(M4zStduZ), label='Moment 4 / (Standard deviation)2 3D')

# Plot 3D du rapport des moments 6 sur la variance :

fig = plt.figure(14)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 6 of uX, uY, uZ on (Standard deviation)3 of uX, uY, uZ of 1280 particles for 3300 dt and St = 0.99")
ax.set_xlabel('Moment 6 / (Standard deviation)3 of uX')
ax.set_ylabel('Moment 6 / (Standard deviation)3 of uY')
ax.set_zlabel('Moment 6 / (Standard deviation)3 of uZ')

ax.plot(np.concatenate(M6xStduX), np.concatenate(M6yStduY), np.concatenate(M6zStduZ), label='Moment 6 / (Standard deviation)3 3D')

plt.show()
