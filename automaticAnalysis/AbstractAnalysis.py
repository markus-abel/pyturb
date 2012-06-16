#!\/usr/bin/python

class AbstractAnalysis(object):
  
  isAnalysisCollection = False
    
  def __init__(self):
    pass
  def __del__(self):
    pass

  def init( self ):
    raise Exception( "Can not call abstract class method AbstractTest.init" )
    
  def exit( self ):
    raise Exception( "Can not call abstract class method AbstractTest.exit" )

  def run( self ):
    raise Exception( "Can not call abstract class method AbstractTest.run" )     
        
  def analysis( self ):
    raise Exception( "Can not call abstract class method AbstractTest.test" )
  
  #def runAnalysis(self,analysisCollection):
    #raise Exception( "Can not run an analysis for abstract class method AbstractAnalysis.runAnalysis" )

    