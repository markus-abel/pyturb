# Dataset analyze

# You have to write by yourself the Stokes number in the title plot.

import h5py
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats.stats


f = h5py.File('St0.99.h5', 'r')    # Reading the file

# Small part to know what kind of file we are using :

h = list(f)

print (h)

x = f['DNS']

x1 = list(x)

print(x1)

x2 = x['BEAM']

print (x2)

z = np.array(x2)

print ("Shape of z :", z.shape)


# Recuperation of the velocity dataset of all particles :

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

print "How many step time do you want for the 2D plots ?"
T1 = input()

print "How many step time do you want for the 3D representation ?"
T2 = input()

"""
All the 2D plots 

"""

# Plot PDF of Ux, decimal :

plt.figure(1)
plt.subplot(121)
plt.title("Pdf of velocities Ux of 1280 particles for St = 0.99")
plt.xlabel("Ux")
plt.ylabel("P(Ux)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(uX[t], bins=100, range=None, normed=True, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=False, color='r', label=None) 
  print "t fig1 =", t
  t = t + 1


# Plot PDF of Ux, log :

plt.subplot(122)
plt.title("Pdf of velocities Ux of 1280 particles for St = 0.99")
plt.xlabel("Ux")
plt.ylabel("P(Ux)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(uX[t], bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=True, color='r', label=None) 
  print "t fig1 =", t
  t = t + 1


# Plot PDF of Uy, decimal :

plt.figure(2)
plt.subplot(121)
plt.title("Pdf of velocities Uy of 1280 particles for St = 0.99")
plt.xlabel("Uy")
plt.ylabel("P(Uy)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(uY[t], bins=100, range=None, normed=True, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=False, color='r', label=None) 
  print "t fig2 =", t
  t = t + 1

# Plot PDF of Uy, log :

plt.figure(2)
plt.subplot(122)
plt.title("Pdf of velocities Uy of 1280 particles for St = 0.99")
plt.xlabel("Uy")
plt.ylabel("P(Uy)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(uY[t], bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=True, color='r', label=None) 
  print "t fig2 =", t 
  t = t + 1

# Plot PDF of Uz, decimal :

plt.figure(3)
plt.subplot(121)
plt.title("Pdf of velocities Uz of 1280 particles for St = 0.99")
plt.xlabel("Uz")
plt.ylabel("P(Uz)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(uZ[t], bins=100, range=None, normed=True, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=False, color='r', label=None) 
  print "t fig3 =", t
  t = t + 1

# Plot PDF of Uz, log :

plt.figure(3)
plt.subplot(122)
plt.title("Pdf of velocities Uz of 1280 particles for St = 0.99")
plt.xlabel("Uz")
plt.ylabel("P(Uz)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(uZ[t], bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=True, color='r', label=None) 
  print "t fig3 =", t
  t = t + 1

"""
Plot 3D

"""

# Plot 3D repartition of U :

dx = np.zeros( (1,np.size(z[0,:]) ))
dy = np.zeros( (1,np.size(z[0,:]) ))
dz = np.zeros( (1,np.size(z[0,:]) ))

dx = 0.01
dy = 0.01
dz = 0.01

fig = plt.figure(4)
  
ax = fig.gca(projection='3d')

ax.set_title("Repartition of velocities U of 1280 particles for St = 0.99 in 3D")
ax.set_xlabel('Ux')
ax.set_ylabel('Uy')
ax.set_zlabel('Uz')

k = 0
while k < T2:

  ax.bar3d(uX[k], uY[k], uZ[k], dx, dy, dz, color='b', zsort='average')

  k = k + 1

  print "t fig 3D =", k

plt.show() 
