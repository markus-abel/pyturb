import numpy as np
import scipy.stats.stats

def analyze(x):

  b = x[:10, 0]
  c = x[:10, 1]

  print ""
  print "time :", b
  print ""
  print "mean :", c
  print ""

  moment2 = scipy.stats.moment(c, moment=2)
  moment3 = scipy.stats.moment(c, moment=3)
  moment4 = scipy.stats.moment(c, moment=4)

  print "Moment 2 = ", moment2
  print "Moment 3 = ", moment3
  print "Moment 4 = ", moment4
