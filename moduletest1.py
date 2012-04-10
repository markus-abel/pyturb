import read1 as r
import analyze1 as a
import scipy.stats.stats

#import pickle
#import numpy as np

# read data

dataOk = r.read_data1("BinariesResults1","rb")
print ""
print "read data are :"
print ""
print dataOk

# analyze data

results = a.analyze(dataOk)

# calc. statistics
#analyze(data)

# write results
#write_results("filename")


