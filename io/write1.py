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

# main program start
# initialize 

t0=0.
T=1.
dt=0.1
N=(T-t0)/dt
print "number of time steps",N
print("How many particles do you want? ")
N_Part = input()


# state of the system
x=np.zeros( [N_Part,N], dtype=float )

tabx = []
mean = np.zeros( N )
time = []

# time loop to count each time steps:

t = 0
while t<T-dt:
	t = t + dt
	time.append(t-dt)

print "Elapsed time :"
print ""
# while loop
t=t0
n=0
while n<N-1 :

	mean[n] = np.mean(x[:,n])
	x[:,n+1]=step(x[:,n],dt)
	t = t + dt	
	n = n+1
	print t
	
tabx.append(x)
TabTime = np.array(time)
TabMean = np.array(mean)
Values = np.column_stack((TabTime,TabMean))

print TabTime
print TabMean
print Values

with open('BinariesResults1', 'wb') as fichier:

	data = pickle.Pickler(fichier,1)	# le 1 correspond au type de format Pickle que je souhaite
	data.dump(Values)

