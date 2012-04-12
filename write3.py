# voici le programme qui genere mes donnees et les ecrit 
# dans un fichier binaire de petite taille (BinariesResults).
# 


import numpy as np
import pickle

# Random walk:
# define a timestep dt
# define the total time to be run T = total number of steps N*dt
# initialize at time t0
# step forward: draw a random number, and add it to the state x(t)
# repeat
# 
# the formula is x(t+dt) = x(t) sqrt(xi)
# with xi a random number 

# define the step in time:

def step(x,dt):

  xi=np.random.normal(0,1,np.size(x))
  x = x + np.sqrt(dt)*xi
  
  return x

def stepy(y, dt):
	
	yi=np.random.normal(0,1,np.size(y))
	y = y + np.sqrt(dt)*yi

	return y

def stepz(z, dt):

	zi=np.random.normal(0,1,np.size(z))
	z = z + np.sqrt(dt)*zi
  
	return z

# main program start
# initialize 

t0=0.
T=1.
dt=0.01
N=(T-t0)/dt
print "number of time steps",N
print("How many particles do you want? ")
N_Part = input()


# state of the system
x=np.zeros( [N_Part,N], dtype=float )
y=np.zeros( [N_Part,N], dtype=float )
z=np.zeros( [N_Part,N], dtype=float )

tabx = []
taby = []
tabz = []
meanx = np.zeros( N )
meany = np.zeros( N )
meanz = np.zeros( N )
time = []

# time loop to count each time steps:

t = 0
while t<T:
  time.append(t)
  t = t + dt  


#print "Elapsed time :"
#print ""
# while loop
t=0
n=0
while n<N-1:
  x[:,n+1]=step(x[:,n],dt)
  y[:,n+1]=step(y[:,n],dt)
  z[:,n+1]=step(z[:,n],dt)
  t = t + dt	
  n = n+1
#  print t

tabx.append(x)
taby.append(y)
tabz.append(z)
TabTime = np.array(time)
	
with open('BinariesResults3', 'wb') as fichier:

	data = pickle.Pickler(fichier,1)	# le 1 correspond au type de format Pickle que je souhaite
	data.dump(TabTime)

	datax = pickle.Pickler(fichier,1)
	datax.dump(tabx)

	datay = pickle.Pickler(fichier,1)
	datay.dump(taby)

	dataz = pickle.Pickler(fichier,1)
	dataz.dump(tabz)
