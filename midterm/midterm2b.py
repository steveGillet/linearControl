import numpy as np

# Define matrix B again
B = np.array([[3, 1, 2],
              [1, 1, 0],
              [-1, 2, 3],
              [2, -1, -2],
              [4, -2, 4],
              [2, 3, 1]])

# Define the vector w
w = np.array([3, 24, 3, -12, 1, 6])

# Solve the system B * [c1, c2, c3] = w
# We can use np.linalg.lstsq to see if there is a solution
solution, residuals, rank, s = np.linalg.lstsq(B, w, rcond=None)

# Check if there are any non-zero residuals (indicating no exact solution)
print(solution, residuals)
