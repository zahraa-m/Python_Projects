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

# math: add 2 vectors in python list
u=[1,0]
v=[0,1]
z=[]
for n, m in zip(u, v):
    z.append(n+m)
print(z)
print(type(z))

# or adding 2 vectors in Numpy
z=[]
u=np.array([1,0])
v=np.array([0,1])
z=u+v
print(z)
print(type(z))

# Scalar
y=np.array([3,4])
print(2*y)

# Product of 2 vectors
u=np.array([1,2])
v=np.array([3,1])
z=u*v
print(z)

# Dot Product
dot_p=np.dot(u, v)
print(dot_p)


