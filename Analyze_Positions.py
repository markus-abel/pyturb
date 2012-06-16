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


# Recuperation des donnees de positions pour toutes les particules:

tabTime = []

X = np.zeros( (np.size(z[:,0]),np.size(z[0,:]) ))
Y = np.zeros( (np.size(z[:,0]),np.size(z[0,:]) ))
Z = np.zeros( (np.size(z[:,0]),np.size(z[0,:]) ))

j = 0
while j < 3300 :

  i = 0
  while i < 1280:
  
    X[j,i] = z[j][i][0]
    Y[j,i] = z[j][i][1]
    Z[j,i] = z[j][i][2]
  
    i = i + 1

  j = j + 1
  
  tabTime.append(j)


# Analyse des positions :

"""
Standard deviation and Moments of positions :

"""

StdX = np.zeros( (np.size(z[:,0]), 1) )
StdY = np.zeros( (np.size(z[:,0]), 1) )
StdZ = np.zeros( (np.size(z[:,0]), 1) )

Moment2x = np.zeros( (np.size(z[:,0]), 1) )
Moment2y = np.zeros( (np.size(z[:,0]), 1) )
Moment2z = np.zeros( (np.size(z[:,0]), 1) )

Moment4x = np.zeros( (np.size(z[:,0]), 1) )
Moment4y = np.zeros( (np.size(z[:,0]), 1) )
Moment4z = np.zeros( (np.size(z[:,0]), 1) )

Moment6x = np.zeros( (np.size(z[:,0]), 1) )
Moment6y = np.zeros( (np.size(z[:,0]), 1) )
Moment6z = np.zeros( (np.size(z[:,0]), 1) )

M2xStdX = np.zeros( (np.size(z[:,0]), 1) )
M2yStdY = np.zeros( (np.size(z[:,0]), 1) )
M2zStdZ = np.zeros( (np.size(z[:,0]), 1) )

M4xStdX = np.zeros( (np.size(z[:,0]), 1) )
M4yStdY = np.zeros( (np.size(z[:,0]), 1) )
M4zStdZ = np.zeros( (np.size(z[:,0]), 1) )

M6xStdX = np.zeros( (np.size(z[:,0]), 1) )
M6yStdY = np.zeros( (np.size(z[:,0]), 1) )
M6zStdZ = np.zeros( (np.size(z[:,0]), 1) )

m = 0 
while m < 3300 :

  StdX[m] = scipy.std(X[m])
  StdY[m] = scipy.std(Y[m])
  StdZ[m] = scipy.std(Z[m])

  Moment2x[m] = scipy.stats.moment(X[m], moment=2)  
  Moment2y[m] = scipy.stats.moment(Y[m], moment=2)
  Moment2z[m] = scipy.stats.moment(Z[m], moment=2)

  Moment4x[m] = scipy.stats.moment(X[m], moment=4)  
  Moment4y[m] = scipy.stats.moment(Y[m], moment=4)
  Moment4z[m] = scipy.stats.moment(Z[m], moment=4)

  Moment6x[m] = scipy.stats.moment(X[m], moment=6)  
  Moment6y[m] = scipy.stats.moment(Y[m], moment=6)
  Moment6z[m] = scipy.stats.moment(Z[m], moment=6)

  M2xStdX[m] = np.divide(Moment2x[m], StdX[m])
  M2yStdY[m] = np.divide(Moment2y[m], StdY[m])
  M2zStdZ[m] = np.divide(Moment2z[m], StdZ[m])

  M4xStdX[m] = np.divide(Moment4x[m], (np.power(StdX[m], 2)) )
  M4yStdY[m] = np.divide(Moment4y[m], (np.power(StdY[m], 2)) )
  M4zStdZ[m] = np.divide(Moment4z[m], (np.power(StdZ[m], 2)) )

  M6xStdX[m] = np.divide(Moment6x[m], (np.power(StdX[m], 3)) )
  M6yStdY[m] = np.divide(Moment6y[m], (np.power(StdY[m], 3)) )
  M6zStdZ[m] = np.divide(Moment6z[m], (np.power(StdZ[m], 3)) )

  m = m + 1


"""
Tous les plots a 1D :

"""


# Plot 1D de la variance :

plt.figure(1)

plt.title("Standard deviation of X, Y, Z of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Standard deviation")
plt.plot(tabTime, StdX)
plt.plot(tabTime, StdY)
plt.plot(tabTime, StdZ)
plt.legend(("Standard deviation of X", "Standard deviation of Y", "Standard deviation of Z"), 'best') 

# Plot 1D des moments 2:

plt.figure(2)

plt.title("Moments 2 of X, Y, Z of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Moment 2")
plt.plot(tabTime, Moment2x)
plt.plot(tabTime, Moment2y)
plt.plot(tabTime, Moment2z)
plt.legend(("Moment 2 of X", "Moment 2 of Y", "Moment 2 of Z"), 'best') 

# Plot 1D des moments 4:

plt.figure(3)

plt.title("Moments 4 of X, Y, Z of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Moment 4")
plt.plot(tabTime, Moment4x)
plt.plot(tabTime, Moment4y)
plt.plot(tabTime, Moment4z)
plt.legend(("Moment 4 of X", "Moment 4 of Y", "Moment 4 of Z"), 'best') 

# Plot 1D des moments 6:

plt.figure(4)

plt.title("Moments 6 of X, Y, Z of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Moment 6")
plt.plot(tabTime, Moment6x)
plt.plot(tabTime, Moment6y)
plt.plot(tabTime, Moment6z)
plt.legend(("Moment 6 of X", "Moment 6 of Y", "Moment 6 of Z"), 'best') 

# Plot 1D du rapport des moments 2 sur la variance :

plt.figure(5)

plt.title("Moments 2 of X, Y, Z on Standard deviation of X, Y, Z of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Moment 2 / Standard deviation")
plt.plot(tabTime, M2xStdX)
plt.plot(tabTime, M2yStdY)
plt.plot(tabTime, M2zStdZ)
plt.legend(("Moment 2 / Standard deviation of X", "Moment 2 / Standard deviation of Y", "Moment 2 / Standard deviation of Z"), 'best') 

# Plot 1D du rapport des moments 4 sur la variance au carre :

plt.figure(6)

plt.title("Moments 4 of X, Y, Z on (Standard deviation)2 of X, Y, Z of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Moment 4 / (Standard deviation)2")
plt.plot(tabTime, M4xStdX)
plt.plot(tabTime, M4yStdY)
plt.plot(tabTime, M4zStdZ)
plt.legend(("Moment 4 / (Standard deviation)2 of X", "Moment 4 / (Standard deviation)2 of Y", "Moment 4 / (Standard deviation)2 of Z"), 'best') 

# Plot 1D du rapport des moments 6 sur la variance au cube :

plt.figure(7)

plt.title("Moments 6 of X, Y, Z on (Standard deviation)3 of X, Y, Z of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Moment 6 / (Standard deviation)3")
plt.plot(tabTime, M6xStdX)
plt.plot(tabTime, M6yStdY)
plt.plot(tabTime, M6zStdZ)
plt.legend(("Moment 6 / (Standard deviation)3 of X", "Moment 6 / (Standard deviation)3 of Y", "Moment 6 / (Standard deviation)3 of Z"), 'best') 

"""
Tous les plots 3D :

"""

# Plot 3D de la variance :

fig = plt.figure(8)
  
ax = fig.gca(projection='3d')

ax.set_title("Standard deviation of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Standard deviation of X')
ax.set_ylabel('Standard deviation of Y')
ax.set_zlabel('Standard deviation of Z')

ax.plot(np.concatenate(StdX), np.concatenate(StdY), np.concatenate(StdZ), label='Standrad deviation 3D')

# Plot 3D des moments 2:

fig = plt.figure(9)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 2 of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Moment 2 of X')
ax.set_ylabel('Moment 2 of Y')
ax.set_zlabel('Moment 2 of Z')

ax.plot(np.concatenate(Moment2x), np.concatenate(Moment2y), np.concatenate(Moment2z), label='Moment 2 3D')

# Plot 3D des moments 4:

fig = plt.figure(10)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 4 of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Moment 4 of X')
ax.set_ylabel('Moment 4 of Y')
ax.set_zlabel('Moment 4 of Z')

ax.plot(np.concatenate(Moment4x), np.concatenate(Moment4y), np.concatenate(Moment4z), label='Moment 4 3D')

# Plot 3D des moments 6:

fig = plt.figure(11)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 6 of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Moment 6 of X')
ax.set_ylabel('Moment 6 of Y')
ax.set_zlabel('Moment 6 of Z')

ax.plot(np.concatenate(Moment6x), np.concatenate(Moment6y), np.concatenate(Moment6z), label='Moment 6 3D')

# Plot 3D du rapport des moments 2 sur la variance :

fig = plt.figure(12)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 2 of X, Y, Z on Standard deviation of X, Y, Z of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Moment 2 / Standard deviation of X')
ax.set_ylabel('Moment 2 / Standard deviation of Y')
ax.set_zlabel('Moment 2 / Standard deviation of Z')

ax.plot(np.concatenate(M2xStdX), np.concatenate(M2yStdY), np.concatenate(M2zStdZ), label='Moment 2 / Standard deviation 3D')

# Plot 3D du rapport des moments 4 sur la variance au carre :

fig = plt.figure(13)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 4 of X, Y, Z on (Standard deviation)2 of X, Y, Z of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Moment 4 / (Standard deviation)2 of X')
ax.set_ylabel('Moment 4 / (Standard deviation)2 of Y')
ax.set_zlabel('Moment 4 / (Standard deviation)2 of Z')

ax.plot(np.concatenate(M4xStdX), np.concatenate(M4yStdY), np.concatenate(M4zStdZ), label='Moment 4 / (Standard deviation)2 3D')

# Plot 3D du rapport des moments 6 sur la variance :

fig = plt.figure(14)
  
ax = fig.gca(projection='3d')

ax.set_title("Moments 6 of X, Y, Z on (Standard deviation)3 of X, Y, Z of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Moment 6 / (Standard deviation)3 of X')
ax.set_ylabel('Moment 6 / (Standard deviation)3 of Y')
ax.set_zlabel('Moment 6 / (Standard deviation)3 of Z')

ax.plot(np.concatenate(M6xStdX), np.concatenate(M6yStdY), np.concatenate(M6zStdZ), label='Moment 6 / (Standard deviation)3 3D')

plt.show()
