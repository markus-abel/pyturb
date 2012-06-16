#!\/usr/bin/python

class AbstractAnalysis(object):
  #isAnalysisCollection =  False

  def __init__(self):
    self.name="Abstract Analhysis"
    pass
  def __del__(self):
    pass
  
  def runAnalysis(self,analysisCollection):
    raise Exception( "Can not run an analysis for abstract class method AbstractAnalysis.runAnalysis" )

      