import read3 as r
import analyze3 as a
import plot3 as p
import finalWrite3_ods as fo
import finalWrite3_txt as ft
import scipy.stats.stats
import numpy as np
from matplotlib import pyplot as plt
# read data
  
dataOk = r.read_data3("BinariesResults3","rb")

time = dataOk[0]
positionsX = dataOk[1]
positionsY = dataOk[2]
positionsZ = dataOk[3]

# analyze data

results = a.analyze(positionsX, positionsY, positionsZ, time)

time = results[0]
meanX = results[1]
meanY = results[2]
meanZ = results[3]
momentX2 = results[4]
momentX3 = results[5]
momentX4 = results[6]
momentY2 = results[7]
momentY3 = results[8]
momentY4 = results[9]
momentZ2 = results[10]
momentZ3 = results[11]
momentZ4 = results[12]

# plot results

old_settings = np.seterr(all='ignore') 
np.seterr(over='raise')
x = np.array(momentX2/momentX4)
y = np.array(momentY2/momentY4)
z = np.array(momentZ2/momentZ4)

p.plotAnalyze(x, y, z, time)

# write results

fo.write_resultso(time, meanX, meanY, meanZ, momentX2, momentY2, momentZ2, momentX3, momentY3, momentZ3, momentX4, momentY4, momentZ4)
ft.write_resultst(time, meanX, meanY, meanZ, momentX2, momentY2, momentZ2, momentX3, momentY3, momentZ3, momentX4, momentY4, momentZ4)

