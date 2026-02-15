import numpy as np
from math import pi
import matplotlib.pyplot as plt
a=0
b=pi
N=1000
h=(b-a)/N
s,d=0,0
def J(m,x):
    d=0
    for k in range(0,N,2):
        s=h*(np.cos(m*(a+k*h)-x*np.sin(a+k*h))+4*(np.cos(m*(a+(k+1)*h)-x*np.sin(a+(k+1)*h)))+np.cos(m*(a+(k+2)*h)-x*np.sin(a+(k+2)*h)))/3    #BESSEL FUNCTION(addition of all lights from cricular aperture)
        d+=s
    return d/pi
x=np.linspace(0,20,200)
J0=[]
J1=[]
J2=[]
for k in x:
   J0.append(J(0,k))
   J1.append(J(1,k))
   J2.append(J(2,k))
plt.plot(x,J0,label="J0(x)")
plt.plot(x,J1,label="J1(x)")
plt.plot(x,J2,label="J2(x)")
plt.show()
t=np.linspace(-1e-6,1e-6,200)
u=np.linspace(-1e-6,1e-6,200)
X,Y=np.meshgrid(t,u)
R=np.sqrt(X**2+Y**2)
k=(2*pi)/(500e-9)
I=np.zeros_like(R)
I = (J(1, k*R)/(k*R))**2    #Intensity of light
I[R==0] = 0.25
plt.imshow(I,
           extent=[-1e-6, 1e-6, -1e-6, 1e-6],
           origin='lower',
           cmap='gray',
           vmax=0.01,      # reduces center brightness so rings show clearly
           interpolation='bilinear')
plt.colorbar()
plt.show()
