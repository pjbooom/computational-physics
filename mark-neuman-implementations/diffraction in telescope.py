import numpy as np
import matplotlib.pyplot as plt
from math import pi
a=0
b=pi
N=1000
h=(b-a)/N
def J(m,x):
  s=(np.cos(m*a)-x*np.sin(a)+np.cos(m*b)-x*np.sin(b))/pi
  for k in range(1,N,2):
    s+=4*(np.cos(m*(a+k*h)-x*np.sin(a+k*h)))
  for k in range(2,N,2):
    s+=2*(np.cos(m*(a+k*h)-x*np.sin(a+k*h)))
  return (s*h)/3
x=np.linspace(0,20,200)
J0=[]
J1=[]
J2=[]
for k in x:
  J0.append(J(0,k))
  J1.append(J(1,k))
  J2.append(J(2,k))
plt.plot(x,J0,label='J0')
plt.plot(x,J1,label='J1')
plt.plot(x,J2,label='J2')
plt.show()
t=np.linspace(-1e-6,1e-6,200)
p=np.linspace(-1e-6,1e-6,200)
X,Y=np.meshgrid(t,p)
R=np.sqrt(X**2+Y**2)
I=np.zeros_like(R)
k=(2*pi)/(500*1e-9)
I = (J(1, k*R)/(k*R))**2
I[R==0] = 0.25
plt.imshow(I,extent=[-1e-6,1e-6,-1e-6,1e-6],origin='lower',cmap='gray',vmax=0.01,interpolation='bilinear')     
plt.colorbar()
plt.show()
