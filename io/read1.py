# Cette partie permet de lire le fichier de donnees (BinariesResults)
# que nous avons genere avant et de l utiliser pour calculer les differents moments
# de la distribution. 

import pickle
import numpy as np

def  read_data1(filename,flag):
  
  with open(filename, flag) as fichier:
    data = pickle.Unpickler(fichier)
    data_recupere = data.load()
  
  return data_recupere
