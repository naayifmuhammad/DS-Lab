import numpy as np

print("Array indexing: slicing")
a1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("a1 =", a1)

b = a1[:2, 1:3]
print("Subarray consisting of the first two rows and columns 1 and 2:", b)

b = a1[1:2, :]
print("Subarray consists of the second row:", b)

print("Accessing columns:")
c = a1[:, 1:2]
print(c, c.shape)

print("Array integer indexing:")
a2 = np.array([[1, 2], [3, 4], [5, 6]])
print("a2 =", a2)

print("Example of array integer indexing:", a2[[0, 1, 2], [0, 1, 0]])
print(a2[[0, 0], [1, 1]])
print(np.array([a2[0, 1], a2[0, 1]]))

a3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("a3 =", a3)

# Create an array of indices
b = np.array([0, 2, 0, 1])
print("b =", b)

print("Select one element from each row of a using the indices in b:")
print("a3 =", a3[np.arange(4), b])

a3[np.arange(4), b] += 10
print("a3 =", a3)

print("Boolean array indexing:")
a = np.array([[1, 2], [3, 4], [5, 6]])
print("a =", a)

bool_idx = (a > 2)
print("Elements greater than 2:", a[bool_idx])
