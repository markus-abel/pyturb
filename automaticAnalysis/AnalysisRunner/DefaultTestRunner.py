#! /usr/bin/python

import time
import sys
import traceback

from AbstractAnalysisRunner import *

def getIndent( indent ):
    return "    " * indent

#implements AbstractAnalysisRunner
#stolen from Karstens DefaultTestRunner class

class DefaultAnalysisRunner( AbstractAnalysisRunner ):
    def __init__( self , indent = 0 , printTree = True ):
        self.results = []
        self.indent = indent
        #self.printTree = printTree  # not needed yet

    def runAnalysisCollectionImpl( self , analysisCollection ):
        for t in analysisCollection.analysiss :
            if t.isAnalysisCollection :
                if self.printTree :
                    print getIndent( self.indent ) + "Starting " + str( t.name )
                    self.indent += 1
                self.runAnalysisCollectionImpl( t )
                if self.printTree:
                    self.indent -= 1
            else:
                self.runAnalysis( t )
    def runAnalysisCollection( self , analysisCollection ):
        t0 = time.time()
        self.runAnalysisCollectionImpl( analysisCollection )
        t1 = time.time()
        print
        print "Run " + str( len( self.results ) ) + " Analysis(s) in " + str( t1 - t0 ) + " seconds."
        numberOfErrors = 0
        for r in self.results:
            if r[0] == False : numberOfErrors += 1
        print str( numberOfErrors ) + " Error(s)"
        
    def runAnalysis( self , analysis ):
        res = []
        t0 = time.time()
        try:
            analysis.init()
            analysis.run()
            res = analysis.analysis()
            analysis.exit()
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            res = [ False , "Exception : " + str( e ) + ", exe_info : " + repr( traceback.format_tb( exc_traceback ) ) ]
        t1 = time.time()
            
        if res[0] == True :
            print getIndent( self.indent ) + "OK : " + analysis.name + ", elapsed time : " + str( t1 - t0 )
            self.results.append( res )
        else :
            print getIndent( self.indent ) + "ERROR : " + analysis.name + ", elapsed time : " + str( t1 - t0 )
            self.results.append( res )
