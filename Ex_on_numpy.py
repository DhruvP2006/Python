import numpy as np
# a = np.array([1, 2, 3], dtype='int16')
# b = np.array([5,6,7])
# print(a*b)
# c = np.array([[1, 2, 3], [12, 23, 34]])
# print(c.ndim)
# print(a.shape)
# print(c.shape) #gives the dimension in rows and columns
# print(a.dtype)
# print(a.itemsize)  #returns number of bytes

# a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
# print(a.shape)
# print(a[1, 5]) #a[row, column]
# print(a[1, -2])
# print(a[0, :]) # particular row
# print(a[:, 3]) # particular column
# print(a[0, 1:6:2])
# a[1, 5] = 20
# print(a)
# a[:, 2] = 1,2
# print(a)

# b = np.array([[[1, 2], [3,4]], [[5,6],[7,8]] ])
# print(b)
# print(b[0,1,1])
# print(b.shape)
# b[:,1,:] = [[9,9], [8,8]]
# print(b)

# print(np.zeros((2,3)))
# print(np.ones((2,3)))
# print(np.full((2,2), 99, dtype='float32'))
# print(np.full_like(a, 4))
# print(np.random.random_sample(a.shape))
# print(np.random.randint(1,28, size=(2,2)))
# print(np.identity(3))

# arr = np.array([[1,2,3], [4,5,6]])
# r1 = np.repeat(arr, 3, axis=0)
# print(r1)

# output = np.ones((5,5))
# print(output)
# z = np.zeros((3,3))
# z[1,1] = 9
# print(z)
# output[1:4, 1:4] = z
# print(output)

