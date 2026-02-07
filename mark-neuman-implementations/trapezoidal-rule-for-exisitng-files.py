#FOR A FILE BASED ONLY
import numpy as np
import matplotlib.pyplot as plt
content=np.loadtxt('/content/velocities.txt')
x=content[:,0]
f=content[:,1]
N=100
distance=np.zeros(len(x))
for i in range(1,len(x)):
  base=0.5*(x[i]-x[i-1])
  area=base*(f[i]+f[i-1])
  distance[i]=distance[i-1]+area
print(distance[-1])
fig,axes=plt.subplots(2,1)
axes[0].plot(x,f)
axes[0].plot(x,distance)
