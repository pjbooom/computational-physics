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
distance=np.zeros(len(t))
for k in range(1,N,2):
  area=h*(f(a+(k-1)*h)+4*f(a+k*h)+f(a+(k+1)*h))/3
  distance[k+1]=distance[k-1]+area
print(distance[-1])
fig,axes=plt.subplots(2,1)
axes[0].plot(t,rate)
axes[1].plot(t,distance)
plt.show()
