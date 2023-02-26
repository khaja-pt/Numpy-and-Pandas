import numpy as np

b=np.array([1,2,3,4])

b

b*2

[i*2 for i in b]

b=np.array([1,2,3,4])

b*2

a=np.array([1,23,4,6,7,8])

a.ndim

 a.shape

m=np.arange(1,10)


m

m=np.arange(1,10,0.5)




m

m

np.linspace(1,10,3)

type(a)

a=np.arange(1,13).reshape(2,-1)

a

a.dtype

A={1,2,"hello"}

A.dtype

a=np.array([[1,2,3],[2,3,4],[3,4,5],[1,2,3]])

a

a.shape

a.dtype

a.ndim

len(a)

m2=np.arange(1,3)

m2

a

a.reshape((2,-1))

a=np.linspace(1,100,30).reshape(3,-1)

a

a.shape

a.dtype

a.ndim

b=a.T

b.shape

b

b.dtype

b.ndim

b[0][1]

#special array
np.zeros(3)

np.zeros(4)

np.zeros((3,3))

a=np.ones((4,4))

a

[a*10 for i in a]

#to avoid null values

np.full((3,3),5)

a

b

b.flatten().ndim

b.shape

np.full((3,3),5)

np.ones([3,3])

np.diag([1,2,3,4])

np.diag([3,3],2)

k=np.full([3,3],3)

k

j=k.flatten()
j

j

j[:5]

j=np.arange(1,13).reshape(3,-1)

j

k=j.flatten()

k

k[:5]

j

j[:2,:2]

j[:,:2]

j

j[:,:3]

j[:,::2]

j[:,(0,2)]

j[1,:2]

j[0,1:3]

j[0][1]=4

j

k=np.arange(1,13)

k

k=k.flatten()

k

k[3:]=4,5,6

k.shape

k[:-1]

k[::-1]

k

a=[1,2,5,6]
b=[2,688,8]

a

b[::-1]

a[2:]=b[::-1]

a

j

j[2:,2:]







