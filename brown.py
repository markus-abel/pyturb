# N_sim: number of simulations
# T: horizon
# dt: step length in years
# sigma: volatility per year
# mu: drift terms (moving average or long-term mean for stock returns)
# S0: initial stock price

from numpy.random import standard_normal
from numpy import array, zeros, sqrt, shape
from pylab import *


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

def Brown():

	Steps=round(T/dt); #Steps in years
	S = zeros([N_Sim, Steps], dtype=float)
	x = range(0, int(Steps), 1)
	
	for j in range(0, N_Sim, 1):
	        S[j,0]= S0
	        for i in x[:-1]:
	                S[j,i+1]=S[j,i]+S[j,i]*(mu-0.5*pow(sigma,2))*dt+sigma*S[j,i]*sqrt(dt)*standard_normal();
	        plot(x, S[j])

# main program start
# initialize 
t0=0.
T=1.
dt=0.01
N=(T-t0)/dt
print N
sigma = 0.5
mu = 0.
N_Part = 3
x=zeros( [N_part,N], dtype=float )
print x

# first method: run each particle from 0 to T
# start again and run etc.
n = 0
while n < N_Sim:
	n = n + 1
	Brown()

# second method: evolve all Particles from t to t+dt
t=t0
while t<T:
  step(x,t)

title('Brownian motion representation for N particles', N_Sim)
xlabel('steps')
ylabel('stock price')
show()

