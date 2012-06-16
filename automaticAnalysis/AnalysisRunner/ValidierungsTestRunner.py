#! /usr/bin/python

import time
import itertools

from AbstractTestRunner import *
from DefaultTestRunner import *

def getIndent( indent ):
    return "    " * indent

class ValidierungsTestRunner( AbstractTestRunner ):
    def __init__(self):
        self.results = []
        self.indent = 0
    def runTestCollection( self , testCollection ):
        t0 = time.time()
        overallTests = 0
        results = []
        detailed_results = []
        for t in testCollection.tests :
            print "Starting " + t.name
            runner = DefaultTestRunner( 1 )
            runner.runTestCollection( t )
            print "Finishing " + t.name
            numberOfErrors = 0
            overallTests += len( runner.results )
            
            for r in runner.results:
                if r[0] == False: numberOfErrors += 1
            
            for r,tt in itertools.izip( runner.results , t.tests ):
                detailed_results.append( [ str( tt ) ] + r )
            
            results.append( [ t.name , numberOfErrors , len( runner.results ) - numberOfErrors , len( runner.results ) ] )
            # print "Running " + str( len( runner.results ) ) + " Test(s), " + str( numberOfErrors ) + " Error(s)"
            print
        t1 = time.time()
        print
        print "Running " + str( overallTests ) + " at all"
        print
        for r in results:
            print r[0] + " : " + str( r[1] ) + " Errors in " + str( r[3] ) + " Tests"  
            
        out = open( "detailed_results.txt" , "w" )
        for r in detailed_results :
            out.write( str( r ) + "\n\n" )
          
