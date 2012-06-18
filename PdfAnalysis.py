import h5py
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import os as os


from  AbstractAnalysis import *

# implements AbstractAnalysis for pdf
# same should be done for structure function and spectrum

class pdfAnalysis( AbstractAnalysis ):
  
  def __init__( self , name, datafile,args = "" ):
    self.name = name
    self.datafile = 'data/St60.h5'
    self.args = args
    try:
      with open(self.datafile) as f: 
	self.f = h5py.File(self.datafile, 'r')    # lecture du fichier
    except IOError as e:
      print 'Oh dear, no data available: check file.', datafile    
#      exit()
    pass
    
  def __del__( self ):
    pass


  def init( self ):
    pass
    
  def exit( self ):
    pass

  def runAnalysis( self , analysis ):
    analysis.init()
    analysis.run()
    res = analysis.analysis()
    analysis.exit()
    if res[0] == True :
      print "OK : " + analysis.name
    else :
      print "ERROR : " + analysis.name

      
  def info(self):
    print "Type of Analysis"+self.name
    print "working on data"+datafile
    print "datafile info"+f
   
  
  
  
  
datafile='data/St60.h5'
A=pdfAnalysis("acceleration",datafile)
A.info()