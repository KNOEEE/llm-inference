import numpy as np


# Reference: https://numpy.org/doc/stable/user/absolute_beginners.html
def array_basics():
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

def create_basic_arrays():
    a = np.zeros((2, 3))
    print(a)
    a = np.ones((2, 3), dtype=np.int32)
    print(a)
    # initialize an array with random values, faster than zeros()
    a = np.empty((2, 3))
    print(a)
    a = np.eye(3)
    print(a)
    a = np.full((2, 3), 7)
    print(a)
    # create an array with a range of values
    a = np.arange(0, 10, 2)
    print(a)
    a = np.linspace(0, 1, 5)
    print(a)

def add_remove_sort():
    a = np.array([1, 2, 3, 4, 5])
    print(a)
    a = np.append(a, [6, 7])
    print(a)
    a = np.insert(a, 0, [0])
    print(a)
    a = np.delete(a, [0, 1])
    print(a)
    a = np.sort(a)
    print(a)

    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    print(np.concatenate((a, b)))
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6]])
    # all the input array dimensions for the concatenation axis must match exactly
    c = np.concatenate((a, b), axis=0)
    print(c)

def add_new_axis():
    a = np.array([1, 2, 3, 4, 5, 6])
    print(a.shape)
    # The core idea of newaxis is to add a new dimension with size 1 to the array.
    # add a new axis to the array
    a2 = a[np.newaxis, :]
    print(a2)
    print(a2.shape)
    # convert the 1D array to a 2D column vector
    col_vector = a[:, np.newaxis]
    print(col_vector)
    print(col_vector.shape)

    b = np.expand_dims(a, axis=1)
    print(b)
    print(b.shape)
    print(b.size == np.prod(b.shape))
    c = np.expand_dims(a, axis=0)
    print(c)
    print(c.shape)
    print(c.size == np.prod(c.shape))

def take_section():
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a[a < 5])

    # boolean mask, a boolean array of the same shape as a, 
    # where each element is True if the corresponding element in a is greater than or equal to 5, 
    # and False otherwise
    five_up = (a >= 5)
    print(a[five_up])

    print(a[a % 2 == 0])

    b = np.nonzero(a < 5)
    print(b)
    list_of_coordinates = list(zip(b[0], b[1]))
    print(list_of_coordinates)
    print(a[b])

    not_there = np.nonzero(a == 42)
    print(not_there)
 
def create_array_from_exsiting_data():
    a1 = np.array([[1, 1], [2, 2]])
    a2 = np.array([[3, 3], [4, 4]])
    a3 = np.vstack((a1, a2))
    print(a3)
    a3 = np.hstack((a1, a2))
    print(a3)
    x = np.arange(1, 25).reshape(2, 12)
    print(x)
    y = np.hsplit(x, 3)
    print(y)
    y = np.hsplit(x, (3, 4))
    print(y)

if __name__ == "__main__":
    reshape_transpose()
