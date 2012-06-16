import pylab as pl
import numpy as np

def pmmap (x,a,z):
  return (x+a*x**z) % 1

# check the klafter and zumofen paper
# this way it does not work

def pmmap2 (x,a,z):
  tmp  = x+a*x**z
  rest = x - (x%1)
  print x,tmp,rest,(tmp%1) + rest
  
  if x>0:
    return (tmp%1) + rest
  else :
    return -(tmp%1) - rest

a=1
z=3
N=10
x=np.zeros(N,dtype="float")
x[0]=1.99999#+0.1*np.pi
for n in range(1,N):
  x[n]=pmmap2(x[n-1],a,z)
  #print x[n],x[n-1]+a*x[n-1]**z

pl.plot(x)
pl.show()


 
