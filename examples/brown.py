# N_sim: number of simulations
# T: horizon
# dt: step length in years
# sigma: volatility per year
# mu: drift terms (moving average or long-term mean for stock returns)
# S0: initial stock price

 #numpy import array, zeros, sqrt, shape
#from numpy.random import *
#romom pylab import *

import numpy as np
import pylab as pl

# Random walk:
# define a timestep dt
# define the total time to be run T = total number of steps N*dt
# initialize at time t0
# step forward: draw a random number, and add it to the state x(t)
# repeat
# 
# the formula is x(t+dt) = x(t) sqrt(xi)
# with xi a random number 

# define the step in time

#def Brown():

  #Steps=round(T/dt); #Steps in years
  #S = zeros([N_Sim, Steps], dtype=float)
  #x = range(0, int(Steps), 1)
  
  #for j in range(0, N_Sim, 1):
          #S[j,0]= S0
          #for i in x[:-1]:
                  #S[j,i+1]=S[j,i]+S[j,i]*(mu-0.5*pow(sigma,2))*dt+sigma*S[j,i]*sqrt(dt)*standard_normal();
          #plot(x, S[j])

def step(x,dt):
  xi=np.random.normal(0,1,np.size(x))
  #print x,xi,np.sqrt(dt)
  x = x + np.sqrt(dt)*xi
  #print x,xi,dt
  
  return x
 
# main program start
# initialize 
t0=0.
T=1.
dt=0.01
N=(T-t0)/dt
print "number of time steps",N
sigma = 0.5
mu = 0.
N_Part = 100
# state of the system
x=np.zeros( [N_Part,N], dtype=float )
variance = np.zeros( N )
#time = linspace()



# while loop
t=t0
n=0
while n<N-1 :
  #print n,x[:,n]
  variance[n] = np.var(x[:,n])
  #print variance[n]
  x[:,n+1]=step(x[:,n],dt)
 
  # calculate mean instantaneous
  # calculate instantaneous variance
  t=t+dt
  n = n+1

# plot var and mean vs. time

pl.plot(variance)
pl.show()
#show()

