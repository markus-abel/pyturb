# Dataset analyze

# You have to write by yourself the Stokes number in the title plot.


import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#import matplotlib.pyplot as plt
import scipy.stats as stats

def pdf_velocity(particle):
  nbins=10

  uX = np.zeros( (np.size(particle[:,0]),np.size(particle[0,:]) ))
  uY = np.zeros( (np.size(particle[:,0]),np.size(particle[0,:]) ))
  uZ = np.zeros( (np.size(particle[:,0]),np.size(particle[0,:]) ))

  Tmax=np.size(particle[:,0])
  NParticles=np.size(particle[0,:])
  NParticles = 3
  print "T,N",Tmax,NParticles

  jrange = range(Tmax)
  for j in jrange:
    for i in range(NParticles):  
      uX[j,i] = particle[j][i][3]     
      uY[j,i] = particle[j][i][4]
      uZ[j,i] = particle[j][i][5]
    
  #print uX[:,1].sort()
  # in case the hist must be stored
  h_tmp=np.zeros(nbins)
  h_uX =np.zeros(nbins)
  binX=pl.linspace(uX[:,NParticles-1].min(),uX[:,NParticles-1].max(),nbins)
  print binX
  pl.figure(1)
  pl.subplot(121)
  for npart in range(NParticles):
    h_tmp=stats.histogram2(uX[:,npart],binX)
    pl.plot(binX,h_tmp)
    h_uX+=h_tmp
  h_uX /= NParticles
  return (binX,h_uX)