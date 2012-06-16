#! /usr/bin/python

from AbstractAnalysis import *

class DummyAnalysis( AbstractAnalysis ):

    name = "Dummy Analysis"

    def __init__( self , name , result = True ):
        self.name = name
        self.result = result
    
    def __del__( self ):
        pass
    
    def init( self ):
        pass
    
    def exit( self ):
        pass

    def run( self ):
        pass
        
    def analysis( self ):
        return [ self.result , "" , None ]
    
