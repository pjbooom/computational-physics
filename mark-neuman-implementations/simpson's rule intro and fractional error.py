import numpy as np
def f(x):
  return x**4-2*x+1
a=0
b=2
N=1000
h=(b-a)/N
s=f(a)+f(b)
for k in range(1,N,2):
  s+=f(a+k*h)
for k in range(2,N,2):
  s+=f(a+k*h)
u=(h*s)/3
print(u)
exact=4.4
error=np.abs(u-exact)/np.abs(exact)
print(100*error)
