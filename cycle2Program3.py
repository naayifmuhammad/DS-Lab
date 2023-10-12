import numpy as np

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[6, 9], [4, 4]], dtype=np.float64)

print("Element wise addition:", np.add(x, x))
print("x =", x)
print("y =", y)
print("Element wise subtraction:", np.subtract(x, y))
print("Element wise multiplication:", np.multiply(x, y))
print("Element wise square root of x:", np.sqrt(x))
print("Matrix multiplication:", np.dot(x, y))
print("Sum of all elements of matrix x:", np.sum(x))
print("Sum of elements in each column of matrix y:", np.sum(y, axis=0))
print("Sum of elements in each row of matrix y:", np.sum(y, axis=1))
print("Transpose of matrix x:", x.T)
