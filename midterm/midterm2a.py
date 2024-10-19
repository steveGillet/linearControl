import numpy as np

# Define the matrix B
B = np.array([[3, 1, 2],
              [1, 1, 0],
              [-1, 2, 3],
              [2, -1, -2],
              [4, -2, 4],
              [2, 3, 1]])

# Define the matrix C
C = np.array([[5, 2, 0],
              [1, 0, 2],
              [2, -3, 1],
              [0, 3, 0],
              [8, 6, -8],
              [3, -1, 5]])

# Define the vector z
z = np.array([18, 2.6, 3.1, 3.0, 34, 7.1])

# Solve for the coordinates in the basis B
coordinates_B = np.linalg.lstsq(B, z, rcond=None)[0]

# Solve for the coordinates in the basis C
coordinates_C = np.linalg.lstsq(C, z, rcond=None)[0]

print(coordinates_B, coordinates_C)
