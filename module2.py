import read2 as r
import analyze2 as a
import plot2 as p
import scipy.stats.stats
import numpy as np
from matplotlib import pyplot as plt
# read data
  
dataOk = r.read_data2("BinariesResults2","rb")

time = dataOk[0]
positions = dataOk[1]

# analyze data

results = a.analyze(positions, time)

time = results[0]
mean = results[1]
moment2 = results[2]
moment3 = results[3]
moment4 = results[4]

print ""
print "Elapsed time : "
print time
print ""
print "Mean : "
print mean
print ""
print "Moment 2 : "
print moment2 
print ""
print "Moment 3 : "
print moment3
print "" 
print "Moment 4 : "
print moment4 

# plot results

old_settings = np.seterr(all='ignore') 
np.seterr(over='raise')
x = np.array(moment2/moment4)

p.plotAnalyze(time, x)

# write results
#write_results("filename")


