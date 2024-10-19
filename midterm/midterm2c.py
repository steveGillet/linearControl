import numpy as np
from numpy.linalg import qr

# Define matrix B
B = np.array([[3, 1, 2],
              [1, 1, 0],
              [-1, 2, 3],
              [2, -1, -2],
              [4, -2, 4],
              [2, 3, 1]])

# Define matrix C
C = np.array([[5, 2, 0],
              [1, 0, 2],
              [2, -3, 1],
              [0, 3, 0],
              [8, 6, -8],
              [3, -1, 5]])

# Perform QR decomposition (Gram-Schmidt) on matrix B to find an orthonormal basis
Q_B, R_B = qr(B)

# Perform QR decomposition (Gram-Schmidt) on matrix C to find an orthonormal basis
Q_C, R_C = qr(C)

# Print the orthonormal bases for both B and C
print("Orthonormal basis for span(B):")
print(Q_B)

print("\nOrthonormal basis for span(C):")
print(Q_C)
