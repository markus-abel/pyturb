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


# Recuperation des donnees de positions pour 3 particules:

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
La moyenne :

"""

Meanx = np.zeros( (np.size(z[:,0]), 1) )
Meany = np.zeros( (np.size(z[:,0]), 1) )
Meanz = np.zeros( (np.size(z[:,0]), 1) )

m = 0 
while m < 3300 :

  Meanx[m] = np.mean(X[m])
  Meany[m] = np.mean(Y[m])
  Meanz[m] = np.mean(Z[m])

  m = m + 1

# Plot 1D :

plt.figure(1)

plt.title("Mean motion of 1280 particles for 3300 dt and St = 0.99")
plt.xlabel("Time")
plt.ylabel("Position")
plt.plot(tabTime, Meanx)
plt.plot(tabTime, Meany)
plt.plot(tabTime, Meanz)
plt.legend(("Mean Value of X", "Mean Value of Y", "Mean Value of Z"), 'best') 

# Plot 3D :

fig = plt.figure(2)
  
ax = fig.gca(projection='3d')

ax.set_title("Mean motion of 1280 particles for 3300 dt and St = 0.99")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.plot(np.concatenate(Meanx), np.concatenate(Meany), np.concatenate(Meanz), label='Mean motion 3D')

plt.show()
