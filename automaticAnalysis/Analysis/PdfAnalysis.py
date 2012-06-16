import h5py
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import os as os


from  AbstractAnalysis import *


class pdfAnalysis( AbstractAnalysis ):
  
  def runAnalysis( self , analysis ):
    analysis.init()
    analysis.run()
    res = analysis.analysis()
    analysis.exit()
    if res[0] == True :
      print "OK : " + analysis.name
    else :
      print "ERROR : " + analysis.name

  
  
  
  
  
  
  
  
  
  
datafile = 'data/St60.h5'
try:
  with open(datafile) as fi: 
    f = h5py.File(datafile, 'r')    # lecture du fichier
except IOError as e:
  print 'Oh dear, no data available: check file.', datafile    
  exit()
  
  