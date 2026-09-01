import numpy as np

# Reference: https://numpy.org/doc/stable/user/absolute_beginners.html
a = np.array([1, 2, 3, 4, 5])
print(a)
print(a[0])
print(a[1:3])
print(a.dtype)
print("a.size:", a.size)
print("a.ndim:", a.ndim)
print("a.shape:", a.shape)
print(a.size == np.prod(a.shape))

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b[0, 0])
print(b.dtype)
print("b.size:", b.size)
print("b.ndim:", b.ndim)
print("b.shape:", b.shape)
print(b.size == np.prod(b.shape))
