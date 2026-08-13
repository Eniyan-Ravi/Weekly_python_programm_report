#matrix operation using numpy
import numpy as np

# Create two matrices
A = np.array([[2, 4, 6],
              [8, 10, 12]])

B = np.array([[1, 3, 5],
              [7, 9, 11]])

print("Matrix A")
print(A)

print("\nMatrix B")
print(B)

print("\nAddition")
print(A + B)

print("\nSubtraction")
print(A - B)

print("\nElement-wise Multiplication")
print(A * B)

print("\nTranspose of Matrix A")
print(A.T)

print("\nFlatten Matrix A")
print(A.flatten())

print("\nReshape Array")
arr = np.arange(1, 13)
print(arr.reshape(3, 4))

print("\nZero Matrix")
print(np.zeros((3, 3)))

print("\nOnes Matrix")
print(np.ones((2, 4)))

print("\nIdentity Matrix")
print(np.eye(4))