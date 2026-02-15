def f(x):
  return x**4-2*x+1
a=0
b=2
N=1000
h=(b-a)/N
s=0.5*(f(a)+f(b))
for k in range(1,N):
  s+=f(a+k*h)
print(s*h)
