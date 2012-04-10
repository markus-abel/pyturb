from matplotlib import pyplot as plt
import numpy as np

def plotAnalyze(X, t):

  plt.title("Moment2/Moment4 function of time")
  plt.ylabel("Moment2/Moment4")
  plt.xlabel("Time")
  plt.plot(X, t)
  plt.show()
