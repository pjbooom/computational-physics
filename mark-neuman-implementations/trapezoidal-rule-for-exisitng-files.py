import numpy as np
import matplotlib.pyplot as plt
content=np.loadtxt('/content/velocities.txt')
f=content[:,0]
t=content[:,1]
distance=np.zeros(len(t))
for k in range(1,len(t)):
  h=(t[k]-t[k-1])
  area=0.5*h*(f[k]+f[k-1])
  distance[k]=disatnce[k-1]+area
fig,axes=plt.subplot(2,1,1)
print(distance[-1])
axes[0].plot(t,f)
axes[1].plot(t,distance)
plt.show()
