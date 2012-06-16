#! /usr/bin/python

import os
import pipes

from AbstractTest import *
from TestFunctions import *
from LogFileParser import *


class StreckenUndLogfileTest( AbstractTest ):
    
    def __init__( self , name , directory , executable , betriebsdaten , fahrspur , logfile , streckenOutput , referenzStrecken , args = "" ):
        self.name = name
        self.directory = directory
        self.executable = os.path.join( directory , executable )
        self.betriebsdaten = os.path.join( directory , betriebsdaten )
        self.fahrspur = os.path.join( directory , fahrspur )
        self.logfile = os.path.join( directory , logfile )
        self.streckenOutput = os.path.join( directory , streckenOutput )
        self.referenzStrecken = os.path.join( directory , referenzStrecken )
        self.args = args
        pass
    
    def __del__( self ):
        pass
    
    def __str__( self ):
        ret = ""
        ret += "Name : " + self.name + "\n"
        ret += "Directory : " + self.directory + "\n"
        ret += "Betriebsdaten : " + self.betriebsdaten + "\n"
        ret += "Fahrspur : " + self.fahrspur + "\n"
        ret += "Logfile : " + self.logfile + "\n"
        ret += "Streckenoutput : " + self.streckenOutput + "\n"
        ret += "Referenzstrecken : " + self.referenzStrecken + "\n"
        return ret

    def init( self ):
        pass
    
    def exit( self ):
        pass
    
    def run( self ):
        runStr  = pipes.quote( self.executable ) + " " + pipes.quote( self.betriebsdaten ) + " "
        runStr += pipes.quote( self.fahrspur ) + " " + pipes.quote( self.logfile ) + " " + pipes.quote( self.streckenOutput )
        for a in self.args:
            runStr += " " + pipes.quote( a )
        os.system( runStr )

    def test( self ):
        res = compareTwoFiles( self.streckenOutput , self.referenzStrecken )
        ret = [ res , "" , None ]
        if res == False:
            ret[1] = " Die Streckenfiles stimmen nicht ueberein : " + self.streckenOutput + " und " + self.referenzStrecken
        return ret
    
    
    
    
    
class StreckenLogfileEntryNumberSingleEOTest( StreckenUndLogfileTest ):  
    """
    falls numberOfEntries = -1 wird die Anzahl nicht beruecksichtigt
    """  

#    def __init__( self , name , directory , executable , betriebsdaten , fahrspur , logfile , streckenOutput , referenzStrecken , args = "" ):    
    def __init__( self , name , directory , executable , betriebsdaten , fahrspur , logfile , streckenOutput , referenzStrecken , numberOfEntries , eoId , args = "" ):
        StreckenUndLogfileTest.__init__( self , name , directory , executable , betriebsdaten , fahrspur , logfile , streckenOutput , referenzStrecken , args )
        self.numberOfEntries = numberOfEntries
        self.eoId = eoId
        self.args = args
    def __str__( self ):
        ret  = StreckenUndLogfileTest.__str__(self)
        ret += "Number of Logfile entries : " + str( self.numberOfEntries ) + "\n"
        ret += "EOID : " + str( self.eoId ) + "\n"
        return ret
    def test( self ):
        ret = StreckenUndLogfileTest.test( self )
        if ret[0] == False: return ret
        self.logEntries = parse_stream( open( self.logfile ) )
        self.logEntriesDict = get_entries_dict( self.logEntries )
        if self.numberOfEntries != -1:
            if len( self.logEntries ) != self.numberOfEntries : return [ False , "Falsche Anzahl befahrener Erkennungsobjekte. Erwartet waren " + str( self.numberOfEntries ) + " , gefunden wurden: " + str( len(logEntries) ) , None ]
        for e in self.logEntries:
            for d in e:
                if d[0] == "E_Stelle" and d[1] != self.eoId : return [ False , "Falsche StellenId " + str( d[1] ) + " gefunden" , None ]
                if d[0] == "A_Stelle" and d[1] != self.eoId : return [ False , "Falsche StellenId " + str( d[1] ) + " gefunden" , None ]                
        return ret
    
    
class StreckenLogfileEntryNumberSingleEOTestFactory:
    def __init__(self , numberOfEntries , eoId ):
        self.numberOfEntries = numberOfEntries
        self.eoId = eoId
    def __call__( self , name , directory , executable , betriebsdaten , fahrspur , logfile , streckenOutput , referenzStrecken , args = "" ):
        return StreckenLogfileEntryNumberSingleEOTest( name , directory , executable , betriebsdaten , fahrspur , logfile , streckenOutput , referenzStrecken , self.numberOfEntries , self.eoId )
        
        
        
class StreckenLogfileEOListTest( StreckenUndLogfileTest ):
    
    def __init__( self , name , directory , executable , betriebsdaten , fahrspur , logfile , streckenOutput , referenzStrecken , eoList , args = "" ):
        StreckenUndLogfileTest.__init__( self , name , directory , executable , betriebsdaten , fahrspur , logfile , streckenOutput , referenzStrecken , args )
        self.eoList = eoList
    def __str__( self ):
        ret  = StreckenUndLogfileTest.__str__( self )
        ret += "EOListe : " + str( self.eoList )
        return ret
    def test( self ):
        ret = StreckenUndLogfileTest.test( self )
        if ret[0] == False: return ret
        logEntries = parse_stream( open( self.logfile ) )
        logEntriesDict = get_entries_dict( logEntries )
        if len( logEntriesDict ) != len( self.eoList ):
            return [ False , "Falsche Anzahl befahrener Erkennungsobjekte! Erwartet waren " + str( len( self.eoList ) ) + " , gefunden wurden: " + str( len(logEntries) ) , None ]
        for (e1,e2) in zip(logEntriesDict,self.eoList) :
            if e1[ "E_Stelle" ] != e2 :
                return [ False , "Falsche StellenID " + str( e1[ "E_Stelle" ] ) + " gefunden!" , None ]
        return ret    
        
        










