# test d'analyse de donnees

import h5py
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

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


# Recuperation des donnees de vitesses pour 3 particules:

tabTime = []

Ux = np.zeros( (np.size(z[:,0]),np.size(z[0,:]) ))
Uy = np.zeros( (np.size(z[:,0]),np.size(z[0,:]) ))
Uz = np.zeros( (np.size(z[:,0]),np.size(z[0,:]) ))

j = 0
while j < 3300 :

  i = 0
  while i < 1280:
  
    Ux[j,i] = z[j][i][3]
    Uy[j,i] = z[j][i][4]
    Uz[j,i] = z[j][i][5]
  
    i = i + 1

  j = j + 1
  
  tabTime.append(j)

# Calcule des accelerations :

Ax = np.zeros( (np.size(z[:,0]), np.size(z[0,:]) ) )
Ay = np.zeros( (np.size(z[:,0]), np.size(z[0,:]) ) )
Az = np.zeros( (np.size(z[:,0]), np.size(z[0,:]) ) )

k = 0
while k < 3300 :

  Ax[k] = (Ux[k] - Ux[k-1]) / (tabTime[k] - tabTime[k-1])
  Ay[k] = (Uy[k] - Uy[k-1]) / (tabTime[k] - tabTime[k-1])
  Az[k] = (Uz[k] - Uz[k-1]) / (tabTime[k] - tabTime[k-1])

  k = k + 1


# Analyse des accelerations :

"""
La moyenne :

"""

MeanAx = np.zeros( (np.size(z[:,0]), np.size(z[0,:]) ) )
MeanAy = np.zeros( (np.size(z[:,0]), np.size(z[0,:]) ) )
MeanAz = np.zeros( (np.size(z[:,0]), np.size(z[0,:]) ) )

m = 0 
while m < 3300 :

  MeanAx[m] = np.mean(Ax[m])
  MeanAy[m] = np.mean(Ay[m])
  MeanAz[m] = np.mean(Az[m])

  m = m + 1

# Plot 1D :

plt.figure(1)

plt.title("Mean acceleration of 1280 particles for 3300 dt and St = 0.99")
plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.plot(tabTime, MeanAx)
plt.plot(tabTime, MeanAy)
plt.plot(tabTime, MeanAz)
plt.legend(("Mean Value of Accx", "Mean Value of Accy", "Mean Value of Accz"), 'best') 

# Plot 3D :

fig = plt.figure(2)
  
ax = fig.gca(projection='3d')

ax.set_title("Mean acceleration of 1280 particles for 3300 dt and St = 0.99")
ax.set_xlabel('Accx')
ax.set_ylabel('Accy')
ax.set_zlabel('Accz')

ax.plot(np.concatenate(MeanAx), np.concatenate(MeanAy), np.concatenate(MeanAz), label='Mean acceleration 3D')

plt.show()
