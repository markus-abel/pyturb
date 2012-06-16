#import pylab as pl
#import numpy as np


from pylab import *


# Gittergroesse
J = 1000
L = 1.0 # Laenge des Systems
a = 0.1 # konstante
z = 1.0 # exponent

# the "velocity"
u = zeros(J)
N = 200#Szeitl. Entwicklung
alpha = 100
t = range(0,N)

# Kopplung: Matrix u_j^{n+1} = (u_j^n)^3 + u_j^n + alpha (u_{j+1}^n - 2u_j^n + u_{j-1}^n)  % 1
#Eintraege auf Diagonale sowie oberer und unterer Diagonale
Diag = (1 -2*alpha)
Upper = alpha
Lower = alpha

A = Diag*diag(ones(J)) + Lower*diag(ones(J-1),-1) + Upper*diag(ones(J-1), 1)

#Eintrage in den Ecken wegen Periodizitaet
A[0 ,-1] = Lower
A[-1, 0] = Upper

# mit Gauss anfangen
#sigma = 5
#u = exp(-arange(-J/2,J/2)**2/2.0/sigma/sigma)/sqrt(2*pi)/sigma/dx

# mit Gleichverteilung anfangen
u = 0.5+0.001*random(J)

# now the particles
# number of particles
Np = 20
taup = 0.1 # damping
v = zeros(Np)

# erstmal nur eins
v=0
x=J/2

#oder doch mehrere
v=zeros(Np)
x=ones(Np)*J/2+random(Np)-0.5
utemp = zeros(Np)

# Step forward in time

xx = zeros((N,Np))
mx = zeros(N) 
mu = zeros(N)
mtu = zeros(N)
uu = zeros((N,J))

for n in t                                 :
  #print x
  uu[n]=u
  u = (dot(A,u) + a*u**z) %1# Zeitschritt
  for i in range(Np):
    utemp[i] =  u[x[i]]
  mu[n]  = mean(u)
  mtu[n] = mean(utemp)
  v = v + 1./taup*( utemp -v )
  x = (divmod(x + v,1)[0]) % J
  xx[n] = x
  mx[n] = mean(x)
  #plot(n*ones(Np),x,'.')

#plot(t,mx)  
show()






"""
#animation vorbereiten
ion()
figure(0)
subplot(111, autoscale_on=False)
axis([x[0], x[-1], 0.0, 10.0])
points = plot(x, u, 'b-') # Anfangspunkte plotten und Graph merken

#Zeitentwicklung und Animation
n = 0
for t_i in t:
	u = dot(A,u) # Zeitschritt
	if (n % 10) == 0: # nur jeden 10. Schritt plotten
		setp( points[0], data=(x,u) ) # Graph aendern
		title('time  %1.4f.' % (t_i))
		draw()
	n += 1

off()
print "Fertig"	
show()
"""

""" Fuer gamma > 1 wird das Verfahren instabil und die Werte u[i] divergieren.
"""




