import numpy as np
from numpy.linalg import qr

# Matrix from the first span set
A = np.array([[1, 0, 1],
              [0, 0, 1],
              [0, 1, 1],
              [1, 0, 0]])

print(A)

# Perform QR decomposition
Q, R = qr(A)

# Check linear independence: If R has any zero diagonal entries, the columns are linearly dependent.
independent = np.all(np.abs(np.diag(R)) > 1e-10)

print(R)

if independent:
    print("The vectors are linearly independent.")
else:
    print("The vectors are linearly dependent.")

# Matrix from the second span set
A = np.array([[1, 0, 1],
              [0, 1, 1],
              [1, 0, 1]])

print(A)

# Perform QR decomposition
Q, R = qr(A)

# Check linear independence: If R has any zero diagonal entries, the columns are linearly dependent.
independent = np.all(np.abs(np.diag(R)) > 1e-10)

print(R)

if independent:
    print("The vectors are linearly independent.")
else:
    print("The vectors are linearly dependent.")
