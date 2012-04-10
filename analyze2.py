import numpy as np
import scipy.stats.stats

def analyze(x, t):
  
  y = np.transpose(x)
  
  Ttime = []
  Tmean = []
  Tmoment2 = []
  Tmoment3 = []
  Tmoment4 = []

  i = 0
  while i < 100:
    
    mean = np.mean(y[i])
    moment2 = scipy.stats.moment((y[i]), moment=2)
    moment3 = scipy.stats.moment((y[i]), moment=3)
    moment4 = scipy.stats.moment((y[i]), moment=4)

    Tmean.append(mean)
    Tmoment2.append(moment2)
    Tmoment3.append(moment3)
    Tmoment4.append(moment4)

    i = i + 1

  Ttime.append(t)
  ti = np.concatenate(Ttime)
  a = np.concatenate(Tmoment2)
  b = np.concatenate(Tmoment3)
  c = np.concatenate(Tmoment4)
  d = np.concatenate(np.column_stack((ti, Tmean, a, b, c)))

#  print y
#  print ""
#  print "Time : "
#  print ti
#  print ""
#  print "Mean : ", Tmean
#  print ""
#  print "Moment 2 : ", a
#  print ""
#  print "Moment 3 : ", b
#  print ""
#  print "Moment 4 : ", c
#  print ""
#  print d

  return ti, Tmean, a, b, c
