from numpy import array
from scipy.linalg import svd

A = array([[1, 2], [3, 4], [5, 6]])
U, s, VT = svd(A)

print("A =", A)
print("Shape of array A:", A.shape)
print("")
print("U =", U)
print("Shape of matrix U:", U.shape)
print("")
print("Sigma (diagonal matrix), s =", s)
print("Shape of matrix sigma:", s.shape)
print("")
print("Transpose Matrix, VT =", VT)
print("Shape of matrix VT:", VT.shape)
