import numpy as np
import scipy.stats.stats

def analyze(x, y, z, t):
  
  x1 = np.transpose(x)
  y1 = np.transpose(y)
  z1 = np.transpose(z)

  Ttime = []
  TmeanX = []
  TmeanY = []
  TmeanZ = []
  TmomentX2 = []
  TmomentX3 = []
  TmomentX4 = []
  TmomentY2 = []
  TmomentY3 = []
  TmomentY4 = []
  TmomentZ2 = []
  TmomentZ3 = []
  TmomentZ4 = []

  i = 0
  while i < 100:
    
    meanX = np.mean(x1[i])
    meanY = np.mean(y1[i])
    meanZ = np.mean(z1[i])
    momentX2 = scipy.stats.moment((x1[i]), moment=2)
    momentX3 = scipy.stats.moment((x1[i]), moment=3)
    momentX4 = scipy.stats.moment((x1[i]), moment=4)
    momentY2 = scipy.stats.moment((y1[i]), moment=2)
    momentY3 = scipy.stats.moment((y1[i]), moment=3)
    momentY4 = scipy.stats.moment((y1[i]), moment=4)
    momentZ2 = scipy.stats.moment((z1[i]), moment=2)
    momentZ3 = scipy.stats.moment((z1[i]), moment=3)
    momentZ4 = scipy.stats.moment((z1[i]), moment=4)


    TmeanX.append(meanX)
    TmeanY.append(meanY)
    TmeanZ.append(meanZ)
    TmomentX2.append(momentX2)
    TmomentX3.append(momentX3)
    TmomentX4.append(momentX4)
    TmomentY2.append(momentY2)
    TmomentY3.append(momentY3)
    TmomentY4.append(momentY4)
    TmomentZ2.append(momentZ2)
    TmomentZ3.append(momentZ3)
    TmomentZ4.append(momentZ4)


    i = i + 1

  Ttime.append(t)
  ti = np.concatenate(Ttime)
  mx = TmeanX
  my = TmeanY
  mz = TmeanZ
  ax = np.concatenate(TmomentX2)
  bx = np.concatenate(TmomentX3)
  cx = np.concatenate(TmomentX4)
  ay = np.concatenate(TmomentY2)
  by = np.concatenate(TmomentY3)
  cy = np.concatenate(TmomentY4)
  az = np.concatenate(TmomentZ2)
  bz = np.concatenate(TmomentZ3)
  cz = np.concatenate(TmomentZ4)

  return ti, mx, my, mz, ax, bx, cx, ay, by, cy, az, bz, cz
