from matplotlib import pyplot as plt
import numpy as np

def plotAnalyze(X, Y, Z, t):

  plt.figure(1)
  plt.subplot(221)
  plt.title("MomentX2/MomentX4 function of time")
  plt.ylabel("MomentX2/MomentX4")
  plt.xlabel("Time")
  plt.plot(t, X)

  plt.subplot(222)
  plt.title("MomentY2/MomentY4 function of time")
  plt.ylabel("MomentY2/MomentY4")
  plt.xlabel("Time")
  plt.plot(t, Y)

  plt.subplot(223)
  plt.title("MomentZ2/MomentZ4 function of time")
  plt.ylabel("MomentZ2/MomentZ4")
  plt.xlabel("Time")
  plt.plot(t, Z)

  plt.show()
