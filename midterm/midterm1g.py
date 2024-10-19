import numpy as np

# Define the matrix of vectors
A = np.array([
    [1, 2, 1],
    [-1, 1, 2],
    [3, 2, -1],
    [0, 4, 4],
    [5, -6, 1]
])

# Perform QR decomposition
Q, R = np.linalg.qr(A)

# Check the rank of the R matrix
rank = np.sum(np.abs(np.diag(R)) > 1e-10)

print(R)

# Determine linear independence
if rank == A.shape[1]:
    print("The set of vectors is linearly independent.")
else:
    print("The set of vectors is linearly dependent.")