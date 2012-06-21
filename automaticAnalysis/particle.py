
class particle:
  
  def __init__(self,):
    self.particle = []

  # helper routine to convert data between
  # formats
  def add(self, p):
    self.particle = append(particle,p)

  # this must be the universal routine to
  # recognize the input data format
  # and conversion to the internal 
  # particle format
  
  def read(self,data):
    pass
  
  def write(self,data):
    pass
  
  
''' our particles consist of Npart particles with
 each consisting of (x,y,z) trace, depending on time,
 i.e. a vector of a 3D vector and (ux,uy,uz), the 
 time-dependent velocity vector. Further data are optional.
 storage is along time, i.e. we store a 6D vector as
 a 2D array with (ntimes x 6) fields for one particle.
 
 Time is assumed equidistant and only the time difference 
  between points is stored.

 Each particle is appended as new (ntimes x 6 array)
 in the third dimension, i.e. eventually we have a 
 Npart x ntimes x 6 array. 
''' 