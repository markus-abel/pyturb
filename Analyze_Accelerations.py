# test d'analyse de donnees

import h5py
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats.stats


f = h5py.File('St60.h5', 'r')    # lecture du fichier

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


# Recuperation des donnees de accelerations pour toutes les particules:

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

# Calcule des accelerations :

Ax = np.zeros( (np.size(z[:,0]), np.size(z[0,:]) ) )
Ay = np.zeros( (np.size(z[:,0]), np.size(z[0,:]) ) )
Az = np.zeros( (np.size(z[:,0]), np.size(z[0,:]) ) )

k = 0
while k < 3300 :

  Ax[k] = (uX[k] - uZ[k-1]) / (tabTime[k] - tabTime[k-1])
  Ay[k] = (uY[k] - uY[k-1]) / (tabTime[k] - tabTime[k-1])
  Az[k] = (uZ[k] - uZ[k-1]) / (tabTime[k] - tabTime[k-1])

  k = k + 1



# Analyse des accelerations :

"""
Standard deviation and Moments of accelerations :

"""

StdaX = np.zeros( (np.size(z[:,0]), 1) )
StdaY = np.zeros( (np.size(z[:,0]), 1) )
StdaZ = np.zeros( (np.size(z[:,0]), 1) )

Moment2ax = np.zeros( (np.size(z[:,0]), 1) )
Moment2ay = np.zeros( (np.size(z[:,0]), 1) )
Moment2az = np.zeros( (np.size(z[:,0]), 1) )

Moment4ax = np.zeros( (np.size(z[:,0]), 1) )
Moment4ay = np.zeros( (np.size(z[:,0]), 1) )
Moment4az = np.zeros( (np.size(z[:,0]), 1) )

Moment6ax = np.zeros( (np.size(z[:,0]), 1) )
Moment6ay = np.zeros( (np.size(z[:,0]), 1) )
Moment6az = np.zeros( (np.size(z[:,0]), 1) )

M2xStdaX = np.zeros( (np.size(z[:,0]), 1) )
M2yStdaY = np.zeros( (np.size(z[:,0]), 1) )
M2zStdaZ = np.zeros( (np.size(z[:,0]), 1) )

M4xStdaX = np.zeros( (np.size(z[:,0]), 1) )
M4yStdaY = np.zeros( (np.size(z[:,0]), 1) )
M4zStdaZ = np.zeros( (np.size(z[:,0]), 1) )

M6xStdaX = np.zeros( (np.size(z[:,0]), 1) )
M6yStdaY = np.zeros( (np.size(z[:,0]), 1) )
M6zStdaZ = np.zeros( (np.size(z[:,0]), 1) )

m = 0 
while m < 3300 :

  StdaX[m] = scipy.std(Ax[m])
  StdaY[m] = scipy.std(Ay[m])
  StdaZ[m] = scipy.std(Az[m])

  Moment2ax[m] = scipy.stats.moment(Ax[m], moment=2)  
  Moment2ay[m] = scipy.stats.moment(Ay[m], moment=2)
  Moment2az[m] = scipy.stats.moment(Az[m], moment=2)

  Moment4ax[m] = scipy.stats.moment(Ax[m], moment=4)  
  Moment4ay[m] = scipy.stats.moment(Ay[m], moment=4)
  Moment4az[m] = scipy.stats.moment(Az[m], moment=4)

  Moment6ax[m] = scipy.stats.moment(Ax[m], moment=6)  
  Moment6ay[m] = scipy.stats.moment(Ay[m], moment=6)
  Moment6az[m] = scipy.stats.moment(Az[m], moment=6)

  M2xStdaX[m] = np.divide(Moment2ax[m], StdaX[m])
  M2yStdaY[m] = np.divide(Moment2ay[m], StdaY[m])
  M2zStdaZ[m] = np.divide(Moment2az[m], StdaZ[m])

  M4xStdaX[m] = np.divide(Moment4ax[m], (np.power(StdaX[m], 2)) )
  M4yStdaY[m] = np.divide(Moment4ay[m], (np.power(StdaY[m], 2)) )
  M4zStdaZ[m] = np.divide(Moment4az[m], (np.power(StdaZ[m], 2)) )

  M6xStdaX[m] = np.divide(Moment6ax[m], (np.power(StdaX[m], 3)) )
  M6yStdaY[m] = np.divide(Moment6ay[m], (np.power(StdaY[m], 3)) )
  M6zStdaZ[m] = np.divide(Moment6az[m], (np.power(StdaZ[m], 3)) )

  m = m + 1


"""
Tous les plots a 1D :

"""


# Plot 1D de la variance :

plt.figure(1)

plt.title("Standard deviation of aX, aY, aZ of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Standard deviation")
plt.plot(tabTime, StdaX)
plt.plot(tabTime, StdaY)
plt.plot(tabTime, StdaZ)
plt.legend(("Standard deviation of aX", "Standard deviation of aY", "Standard deviation of aZ"), 'best') 

# Plot 1D des moments 2:

plt.figure(2)

plt.title("Moments 2 of aX, aY, aZ of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Moment 2")
plt.plot(tabTime, Moment2ax)
plt.plot(tabTime, Moment2ay)
plt.plot(tabTime, Moment2az)
plt.legend(("Moment 2 of aX", "Moment 2 of aY", "Moment 2 of aZ"), 'best') 

# Plot 1D des moments 4:

plt.figure(3)

plt.title("Moments 4 of aX, aY, aZ of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Moment 4")
plt.plot(tabTime, Moment4ax)
plt.plot(tabTime, Moment4ay)
plt.plot(tabTime, Moment4az)
plt.legend(("Moment 4 of aX", "Moment 4 of aY", "Moment 4 of aZ"), 'best') 

# Plot 1D des moments 6:

plt.figure(4)

plt.title("Moments 6 of aX, aY, aZ of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Moment 6")
plt.plot(tabTime, Moment6ax)
plt.plot(tabTime, Moment6ay)
plt.plot(tabTime, Moment6az)
plt.legend(("Moment 6 of aX", "Moment 6 of aY", "Moment 6 of aZ"), 'best') 

# Plot 1D du rapport des moments 2 sur la variance :

plt.figure(5)

plt.title("Moments 2 of aX, aY, aZ on Standard deviation of aX, aY, aZ of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Moment 2 / Standard deviation")
plt.plot(tabTime, M2xStdaX)
plt.plot(tabTime, M2yStdaY)
plt.plot(tabTime, M2zStdaZ)
plt.legend(("Moment 2 / Standard deviation of aX", "Moment 2 / Standard deviation of aY", "Moment 2 / Standard deviation of aZ"), 'best') 

# Plot 1D du rapport des moments 4 sur la variance au carre :

plt.figure(6)

plt.title("Moments 4 of aX, aY, aZ on (Standard deviation)2 of aX, aY, aZ of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Moment 4 / (Standard deviation)2")
plt.plot(tabTime, M4xStdaX)
plt.plot(tabTime, M4yStdaY)
plt.plot(tabTime, M4zStdaZ)
plt.legend(("Moment 4 / (Standard deviation)2 of aX", "Moment 4 / (Standard deviation)2 of aY", "Moment 4 / (Standard deviation)2 of aZ"), 'best') 

# Plot 1D du rapport des moments 6 sur la variance au cube :

plt.figure(7)

plt.title("Moments 6 of aX, aY, aZ on (Standard deviation)3 of aX, aY, aZ of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Moment 6 / (Standard deviation)3")
plt.plot(tabTime, M6xStdaX)
plt.plot(tabTime, M6yStdaY)
plt.plot(tabTime, M6zStdaZ)
plt.legend(("Moment 6 / (Standard deviation)3 of aX", "Moment 6 / (Standard deviation)3 of aY", "Moment 6 / (Standard deviation)3 of aZ"), 'best') 

"""
Tous les plots 3D :

"""

# Plot 3D de la variance :

fig = plt.figure(8)
  
ax = fig.gca(projection='3d')

ax.set_title("Standard deviation of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Standard deviation of aX')
ax.set_ylabel('Standard deviation of aY')
ax.set_zlabel('Standard deviation of aZ')

ax.plot(np.concatenate(StdaX), np.concatenate(StdaY), np.concatenate(StdaZ), label='Standrad deviation 3D')

# Plot 3D des moments 2:

fig = plt.figure(9)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 2 of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Moment 2 of aX')
ax.set_ylabel('Moment 2 of aY')
ax.set_zlabel('Moment 2 of aZ')

ax.plot(np.concatenate(Moment2ax), np.concatenate(Moment2ay), np.concatenate(Moment2az), label='Moment 2 3D')

# Plot 3D des moments 4:

fig = plt.figure(10)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 4 of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Moment 4 of aX')
ax.set_ylabel('Moment 4 of aY')
ax.set_zlabel('Moment 4 of aZ')

ax.plot(np.concatenate(Moment4ax), np.concatenate(Moment4ay), np.concatenate(Moment4az), label='Moment 4 3D')

# Plot 3D des moments 6:

fig = plt.figure(11)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 6 of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Moment 6 of aX')
ax.set_ylabel('Moment 6 of aY')
ax.set_zlabel('Moment 6 of aZ')

ax.plot(np.concatenate(Moment6ax), np.concatenate(Moment6ay), np.concatenate(Moment6az), label='Moment 6 3D')

# Plot 3D du rapport des moments 2 sur la variance :

fig = plt.figure(12)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 2 of aX, aY, aZ on Standard deviation of aX, aY, aZ of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Moment 2 / Standard deviation of aX')
ax.set_ylabel('Moment 2 / Standard deviation of aY')
ax.set_zlabel('Moment 2 / Standard deviation of aZ')

ax.plot(np.concatenate(M2xStdaX), np.concatenate(M2yStdaY), np.concatenate(M2zStdaZ), label='Moment 2 / Standard deviation 3D')

# Plot 3D du rapport des moments 4 sur la variance au carre :

fig = plt.figure(13)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 4 of aX, aY, aZ on (Standard deviation)2 of aX, aY, aZ of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Moment 4 / (Standard deviation)2 of aX')
ax.set_ylabel('Moment 4 / (Standard deviation)2 of aY')
ax.set_zlabel('Moment 4 / (Standard deviation)2 of aZ')

ax.plot(np.concatenate(M4xStdaX), np.concatenate(M4yStdaY), np.concatenate(M4zStdaZ), label='Moment 4 / (Standard deviation)2 3D')

# Plot 3D du rapport des moments 6 sur la variance :

fig = plt.figure(14)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 6 of aX, aY, aZ on (Standard deviation)3 of aX, aY, aZ of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Moment 6 / (Standard deviation)3 of aX')
ax.set_ylabel('Moment 6 / (Standard deviation)3 of aY')
ax.set_zlabel('Moment 6 / (Standard deviation)3 of aZ')

ax.plot(np.concatenate(M6xStdaX), np.concatenate(M6yStdaY), np.concatenate(M6zStdaZ), label='Moment 6 / (Standard deviation)3 3D')

plt.show()
