#! /usr/bin/python

from AbstractAnalysisRunner import *

class SimpleAnalysisRunner( AbstractTestRunner ):

    def runAnalysisCollection( self , analysisCollection ):
        for t in analysisCollection.analysiss :
            if t.isTestCollection :
                self.runTestCollection( t )
            else:
                self.runTest( t )

# implements  AbstractAnalysisRunner.runAnalysis
    def runAnalysis( self , analysis ):
        analysis.init()
        analysis.run()
        res = analysis.analysis()
        analysis.exit()
        if res[0] == True :
            print "OK : " + analysis.name
        else :
            print "ERROR : " + analysis.name
