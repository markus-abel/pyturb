# Voici la suite de ce que je vous ai envoye la semaine derniere
# De la meme maniere pour lancer j utilise directement Ipython -pylab

# Je ne sais pas encore ce que vous voulez dans les proprietes de 
# le fonction aleatoire donc je n y touche pas trop.
import numpy as np
import pylab as plt


def aleat():
	mu, sigma = 0, 1
	s = np.random.normal(mu, sigma, 20)
	plt.figure(1)
	plt.subplot(221)
	count, bins, ignored = plt.hist(s, 30, color='green', normed=True)
	plt.plot(bins, 1/(sigma*np.sqrt(2*np.pi))*np.exp( -(bins - mu)**2 / (2*sigma**2)), linewidth=2, color='r')
	plt.title("Premiere approche de la representation d une PDF")
	
	x1 = np.mean(s)
	x2 = np.mean(s * s)
	x3 = np.mean(s) * np.mean(s)
	x4 = x2 - x3  

	return x1
	return x4


# Je demande a l utilisateur combien de lances il veut faire

print("Combien de lances voulez vous faire? ")
N = input()
n = 0

tabx1 = []
tabx4 = []

while n<N:
	n = n + 1
	a = aleat()
	
	tabx1.append(a)
	tabx4.append(a)

# Je place les valeurs obtenues dans un tableau que je cree a cote pour 
# faire facilement la representation graphique.

plt.figure(1)
plt.subplot(222)
plt.title("Moyenne en fonction du nombre de lances N")
plt.plot(tabx1)
plt.grid(True)

plt.figure(1)
plt.subplot(223)
plt.title("Variance en fonction du log du nombre de lances N")
plt.semilogx(tabx4)
plt.grid(True)

plt.show()
