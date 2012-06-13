# test d'analyse de donnees

import h5py
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

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


# Analyse des vitesses :

"""
La moyenne :

"""

MeanUx = np.zeros( (np.size(z[:,0]), 1) )
MeanUy = np.zeros( (np.size(z[:,0]), 1) )
MeanUz = np.zeros( (np.size(z[:,0]), 1) )

m = 0 
while m < 3300 :

  MeanUx[m] = np.mean(Ux[m])
  MeanUy[m] = np.mean(Uy[m])
  MeanUz[m] = np.mean(Uz[m])

  m = m + 1

# Plot 1D :

plt.figure(1)

plt.title("Mean velocity of 1280 particles for 3300 dt and St = 60")
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.plot(tabTime, MeanUx)
plt.plot(tabTime, MeanUy)
plt.plot(tabTime, MeanUz)
plt.legend(("Mean Value of Ux", "Mean Value of Uy", "Mean Value of Uz"), 'best') 

# Plot 3D :

fig = plt.figure(2)
  
ax = fig.gca(projection='3d')

ax.set_title("Mean velocity of 1280 particles for 3300 dt and St = 60")
ax.set_xlabel('Ux')
ax.set_ylabel('Uy')
ax.set_zlabel('Uz')

ax.plot(np.concatenate(MeanUx), np.concatenate(MeanUy), np.concatenate(MeanUz), label='Mean velocity 3D')

plt.show()
