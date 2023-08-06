import numpy as np
from numpy.random import randint

# NUMPY IS FOR NUMERICAL & MATHEMATICAL

# to convert a list to an array
print(np.array([1, 2, 3]))

# to generate an array with a range
print(np.arange(-2, 3))

# to generate an array with a range and skip the numbers in-between
print(np.arange(-2, 3, 2))

# to get the ZERO's with multi dim
# default is float
print(np.zeros((2, 3), np.int8))

# to get the ZERO's with one dim
print(np.zeros(3, np.int8))

# to generate the random numbers b/w 0-9
print(randint(0, 10))

# to generate the 5 random numbers b/w 0-9
print(randint(0, 10, 5))

# to generate the 2D array(5 rows & 4 columns) b/w 0-9
print(randint(0, 10, (5, 4)))

# to change the dimensions of the original array
print(np.array([[0, 1, 2],
                [3, 4, 5]]).reshape(3, 2))

print(type(list(range(0, 3))))

print(type(np.arange(0, 3)))

mat = np.arange(0, 100).reshape(10, 10)
print(mat[5, 5])
print(mat[5][5])

print(mat[2:3, 0:3])

print(mat < 20)
print(mat[mat < 50])
