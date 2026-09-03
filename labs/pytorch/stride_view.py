import numpy as np

def view():
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    b1 = a[0:2, 1:3]
    print(b1)
    b1[0, 0] = 100
    print(a)

    b2 = a[0:2, 1:3].copy()  # deep copy
    b2[0, 0] = 200
    print(b2)
    print(a)

def broadcast():
    # Broadcasting is a powerful mechanism 
    # that allows NumPy to work with arrays of different shapes when performing arithmetic operations. 
    # It automatically expands the smaller array along the dimensions of the larger array 
    # so that they have compatible shapes.
    data = np.array([1.0, 2.0])
    data *= 1.6
    print(data)
    
def reshape_transpose():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(a)
    b = a.reshape((3, 2))
    print(b)
    print(b.transpose())
    c = a.T
    print(c)

if __name__ == "__main__":
    broadcast()
