import numpy as np
import matplotlib.pyplot as plt
def f(t):
  return np.exp(-t**2)
t=np.arange(0,3.1,0.1)
rate=f(t)
a=0
b=3
h=0.1
N=int((b-a)/h)
s=f(a)+f(b)
for k in range(1,N,2):
  s+=4*f(a+k*h)
for k in range(2,N,2):
  s+=2*f(a+k*h)
print((h*s)/3)
plt.plot(t,rate)
plt.show()
