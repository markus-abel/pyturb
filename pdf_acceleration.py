# Dataset analyze

# You have to write by yourself the Stokes number in the title plot.

import h5py
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats.stats


f = h5py.File('St60.h5', 'r')    # Reading the file

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

# Calculating of accelerations :

Ax = np.zeros( (np.size(z[:,0]), np.size(z[0,:]) ) )
Ay = np.zeros( (np.size(z[:,0]), np.size(z[0,:]) ) )
Az = np.zeros( (np.size(z[:,0]), np.size(z[0,:]) ) )

k = 0
while k < 3300 :

  Ax[k] = (uX[k] - uZ[k-1]) / (tabTime[k] - tabTime[k-1])
  Ay[k] = (uY[k] - uY[k-1]) / (tabTime[k] - tabTime[k-1])
  Az[k] = (uZ[k] - uZ[k-1]) / (tabTime[k] - tabTime[k-1])

  k = k + 1


print "How many step time do you want for the 2D plots ?"
T1 = input()

print "How many step time do you want for the 3D representation ?"
T2 = input()

"""
All the 2D plots 

"""

# Plot PDF of AccX, decimal :

plt.figure(1)
plt.subplot(121)
plt.title("Pdf of Accelerations AccX of 1280 particles for St = 60")
plt.xlabel("AccX")
plt.ylabel("P(AccX)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(Ax[t], bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=False, color='r', label=None) 
  print "t fig1.1 =", t
  t = t + 1

# Plot PDF of absolute value of AccX, decimal :

plt.figure(1)
plt.subplot(122)
plt.title("Pdf of absolute value of Accelerations AccX of 1280 particles for St = 60")
plt.xlabel("|AccX|")
plt.ylabel("P(|AccX|)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(np.abs(Ax[t]), bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=False, color='r', label=None) 
  print "t fig1.2 =", t
  t = t + 1

#regression = np.polyfit(x, np.abs(Ax), 1)
#plt.plot(regression)


# Plot PDF of AccX, log :

plt.figure(2)
plt.subplot(121)
plt.title("Pdf of Accelerations AccX of 1280 particles for St = 60")
plt.xlabel("AccX")
plt.ylabel("P(AccX)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(Ax[t], bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=True, color='r', label=None) 
  print "t fig2.1 =", t
  t = t + 1

# Plot PDF of absolute value of AccX, log :

plt.figure(2)
plt.subplot(122)
plt.title("Pdf of absolute value of Accelerations AccX of 1280 particles for St = 60")
plt.xlabel("|AccX|")
plt.ylabel("P(|AccX|)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(np.abs(Ax[t]), bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=True, color='r', label=None)   
  print "t fig2.2 =", t
  t = t + 1

# Plot PDF of AccY, decimal :

plt.figure(3)
plt.subplot(121)
plt.title("Pdf of accelerations AccY of 1280 particles for St = 60")
plt.xlabel("AccY")
plt.ylabel("P(AccY)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(Ay[t], bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=False, color='r', label=None) 
  print "t fig3.1 =", t
  t = t + 1

# Plot PDF of absolute value of AccY, decimal :

plt.figure(3)
plt.subplot(122)
plt.title("Pdf of absolute value of accelerations AccY of 1280 particles for St = 60")
plt.xlabel("|AccY|")
plt.ylabel("P(|AccY|)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(np.abs(Ay[t]), bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=False, color='r', label=None) 
  print "t fig3.2 =", t
  t = t + 1

# Plot PDF of AccY, log :

plt.figure(4)
plt.subplot(121)
plt.title("Pdf of accelerations AccY of 1280 particles for St = 60")
plt.xlabel("AccY")
plt.ylabel("P(AccY)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(Ay[t], bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=True, color='r', label=None) 
  print "t fig4.1 =", t 
  t = t + 1

# Plot PDF of absolute value of AccY, log :

plt.figure(4)
plt.subplot(122)
plt.title("Pdf of obsolute value of accelerations AccY of 1280 particles for St = 60")
plt.xlabel("|AccY|")
plt.ylabel("P(|AccY|)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(np.abs(Ay[t]), bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=True, color='r', label=None) 
  print "t fig4.2 =", t 
  t = t + 1

# Plot PDF of AccZ, decimal :

plt.figure(5)
plt.subplot(121)
plt.title("Pdf of Acceleration AccZ of 1280 particles for St = 60")
plt.xlabel("AccZ")
plt.ylabel("P(AccZ)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(Az[t], bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=False, color='r', label=None) 
  print "t fig5.1 =", t
  t = t + 1

# Plot PDF of absolute value of AccZ, decimal :

plt.figure(5)
plt.subplot(122)
plt.title("Pdf of absolute value of Acceleration AccZ of 1280 particles for St = 60")
plt.xlabel("|AccZ|")
plt.ylabel("P(|AccZ|)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(np.abs(Az[t]), bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=False, color='r', label=None) 
  print "t fig5.2 =", t
  t = t + 1

# Plot PDF of AccZ, log :

plt.figure(6)
plt.subplot(121)
plt.title("Pdf of Accelerations AccZ of 1280 particles for St = 60")
plt.xlabel("AccZ")
plt.ylabel("P(AccZ)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(Az[t], bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=True, color='r', label=None) 
  print "t fig6.1 =", t
  t = t + 1

# Plot PDF of absolute value of AccZ, log :

plt.figure(6)
plt.subplot(122)
plt.title("Pdf of absolute value of Accelerations AccZ of 1280 particles for St = 60")
plt.xlabel("|AccZ|")
plt.ylabel("P(|AccZ|)")
plt.grid(color='black', linestyle='-', linewidth=0.5)
  
t = 0
while t < T1:

  plt.hist(np.abs(Az[t]), bins=100, range=None, normed=False, cumulative=False, bottom=None, histtype='barstacked', align='mid', orientation='vertical', rwidth=None, log=True, color='r', label=None) 
  print "t fig6.2 =", t
  t = t + 1

# Plot 3D repartition of Acc :

dx = np.zeros( (1,np.size(z[0,:]) ))
dy = np.zeros( (1,np.size(z[0,:]) ))
dz = np.zeros( (1,np.size(z[0,:]) ))

dx = 0.001
dy = 0.001
dz = 0.001

fig = plt.figure(7)
  
ax = fig.gca(projection='3d')

ax.set_title("Repartition of Accelerations Acc of 1280 particles for St = 60 in 3D")
ax.set_xlabel('AccX')
ax.set_ylabel('AccY')
ax.set_zlabel('AccZ')

k = 0
while k < T2:

  ax.bar3d(Ax[k], Ay[k], Az[k], dx, dy, dz, color='b', zsort='average')

  k = k + 1

  print "t fig1 3D =", k

# Test for absolute value of accelerations :

fig = plt.figure(8)
  
ax = fig.gca(projection='3d')

ax.set_title("Repartition of absolute value of Accelerations Acc of 1280 particles for St = 60 in 3D")
ax.set_xlabel('|AccX|')
ax.set_ylabel('|AccY|')
ax.set_zlabel('|AccZ|')

k = 0
while k < T2:

  ax.bar3d(np.abs(Ax[k]), np.abs(Ay[k]), np.abs(Az[k]), dx, dy, dz, color='b', zsort='average')

  k = k + 1

  print "t fig2 3D =", k

plt.show() 
