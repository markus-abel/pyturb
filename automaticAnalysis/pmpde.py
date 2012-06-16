#import pylab as pl
#import numpy as np


from pylab import *
"""
Try to integrate du/dt = au^z + D \Delta u
"""


# Gittergroesse
J = 128
L = 1.0 # Laenge des Systems
dx = L/J

a = 0.0 # konstante
z = 1.0 # exponent
D = 0.1 # Diffusion = Kopplung

x = arange(J)*dx
t_end = 5.0*L*L/D # typische Zeitskale L^2/D


# Stabilitaetskriterium: 2*D*dt/dx^2 <= 1
gamma = 0.5
dt = gamma*dx*dx/(2*D)
N=t_end/dt
print "dt:", dt, "dx:", dx, "t_end:", t_end, "Schritte:", N
# the "velocity"
u = zeros(J)
alpha =  D*dt/dx/dx
t = linspace(0, t_end, N)


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
sigma = 5
u = exp(-arange(-J/2,J/2)**2/2.0/sigma/sigma)/sqrt(2*pi)/sigma/dx

# mit Gleichverteilung anfangen
#u = 0.5+0.001*random(J)


#animation vorbereiten
ion()
figure(0)
subplot(111, autoscale_on=False)
axis([x[0], x[-1], 0.0, 10.0])
points = plot(x, u, 'b-') # Anfangspunkte plotten und Graph merken

#Zeitentwicklung und Animation
n = 0
a = 0.1
for t_i in t:
  a=0.1*(random(1)-0.5)
  u = dot(A,u) + a*u**z # Zeitschritt
  if (n % 10) == 0: # nur jeden 10. Schritt plotten
    setp( points[0], data=(x,u) ) # Graph aendern
    title('time  %1.4f.' % (t_i))
    draw()
  n += 1

ioff()
print "Fertig"	
show()


""" Fuer gamma > 1 wird das Verfahren instabil und die Werte u[i] divergieren.
"""


