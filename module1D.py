import pickle 
import numpy as np

#generate data from a random walk
def step(x,dt):

  xi=np.random.normal(0,1,np.size(x))
  x = x + np.sqrt(dt)*xi
  
  return x
  
  
# read data from file either binary or ascii data
# depending on flag

def  read_dataV1(filename,flag):
  
  with open(filename, flag) as fichier:
    datat = pickle.Unpickler(fichier)
    datat_recupere = datat.load()
  
    datav2 = pickle.Unpickler(fichier)
    datav2_recupere = datav2.load()

  return datat_recupere, datav2_recupere

# write data binary
# flag = wb writes binary data

def  write_dataV1(filename,flag):
  with open(filename, flag) as fichier:

    datat = pickle.Pickler(fichier,1)
    datat.dump(TabTime)

    datav2 = pickle.Pickler(fichier,1)
    datav2.dump(tabv2)
    
  return 0

def write_resultso(t, mean, m2, m3, m4):

  finalResultso = open("Finalo.ods", "w")

  finalResultso.write("Time:")
  finalResultso.write(" ")
  finalResultso.write("Mean:")
  finalResultso.write(" ")
  finalResultso.write("Moment2:")
  finalResultso.write(" ")
  finalResultso.write("Moment3:")
  finalResultso.write(" ")
  finalResultso.write("Moment4:")
  finalResultso.write("\n")
  
  i = 0
  while i < 100:
  
    finalResultso.write(str(t[i]))
    finalResultso.write(" ")
    finalResultso.write(str(mean[i]))
    finalResultso.write(" ")
    finalResultso.write(str(m2[i]))
    finalResultso.write(" ")
    finalResultso.write(str(m3[i]))
    finalResultso.write(" ")
    finalResultso.write(str(m4[i]))
    finalResultso.write("\n")

    i = i + 1

  finalResultso.close()


def write_resultst(t, mean, m2, m3, m4):

  finalResultst = open("Finalt.txt", "w")

  finalResultst.write("Time:")
  finalResultst.write("     ")
  finalResultst.write("Mean:")
  finalResultst.write("       ")
  finalResultst.write("Moment2:")
  finalResultst.write("           ")
  finalResultst.write("Moment3:")
  finalResultst.write("           ")
  finalResultst.write("Moment4:")
  finalResultst.write("\n")
  
  i = 0
  while i < 100:
  
    finalResultst.write(str(t[i]))
    finalResultst.write("   ")
    finalResultst.write(str(mean[i]))
    finalResultst.write("   ")
    finalResultst.write(str(m2[i]))
    finalResultst.write("   ")
    finalResultst.write(str(m3[i]))
    finalResultst.write("   ")
    finalResultst.write(str(m4[i]))
    finalResultst.write("\n")

    i = i + 1

  finalResultst.close()




# analyzes data and writes moments and/or pdf

def analyze(v, t):
  
  vt = np.transpose(v)
  
  Ttime = []
  Tmean = []

  N_moments=4
  moments=np.zeros((N_moments,t.size))
  m=0
  while m<N_moments:
    moments[m] = np.transpose( scipy.stats.moment(vt, moment=2, axis=1) )
    m+=1

  Ttime.append(t)
  ti = np.concatenate(Ttime)

  return ti, Tmean, moments
