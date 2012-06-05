import module1D as m
import scipy.stats.stats
#import numpy as np
from matplotlib import pyplot as plt
from os import path, access, R_OK  # W_OK for write permission.

# read data


PATH='./BinariesResultsVelocity1'

if path.exists(PATH) and path.isfile(PATH) and access(PATH, R_OK):
  print "File exists and is readable"
  dataOk = m.read_dataV1(PATH,"rb")
else:
  print "Either file is missing or is not readable"
  print "exiting!"
  exit()


time = dataOk[0]
velocities = dataOk[1]

# analyze data

results = m.analyze(velocities, time)

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

m.write_resultso(time, mean, moment2, moment3, moment4)
m.write_resultst(time, mean, moment2, moment3, moment4)


