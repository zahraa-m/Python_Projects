# NumPy is a python library for large multi-dimensional arrays and matrices
import numpy as np
x = np.array([0, 1, 2, 3, 4])
print(type(x))
print(x.dtype)
print(x.size)
print(x.ndim)

# indexing
x[0]=40
print(x)
x[1:3]=100, 200
print(x)

# math: add 2 vecters
u=np.array([1,0])
v=np.array([0,1])
z=[]
for n, m in zip(u, v):
    z.append(n+m)
print(z)

#or
z=[]
z=u+v
print(z)



