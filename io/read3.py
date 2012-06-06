# Cette partie permet de lire le fichier de donnees (BinariesResults)
# que nous avons genere avant et de l utiliser pour calculer les differents moments
# de la distribution. 

import pickle
import numpy as np

def  read_data3(filename,flag):
  
  with open(filename, flag) as fichier:
    data = pickle.Unpickler(fichier)
    data_recupere = data.load()
  
    datax = pickle.Unpickler(fichier)
    datax_recupere = datax.load()

    datay = pickle.Unpickler(fichier)
    datay_recupere = datay.load()

    dataz = pickle.Unpickler(fichier)
    dataz_recupere = dataz.load()

  a = data_recupere
  e = datax_recupere
  f = datay_recupere
  g = dataz_recupere

  return a, e, f, g

