import matplotlib.pyplot as plt
import numpy as np

# Define the vector A and the measured vector y
A = np.array([2, 1])
y = np.array([3, 4])

# Calculate the least-squares estimate for x
x_est = 2
Ax = x_est * A

# Create the figure and axis
plt.figure(figsize=(6, 6))
ax = plt.gca()

# Plot the vector y (measured data)
plt.quiver(0, 0, y[0], y[1], angles='xy', scale_units='xy', scale=1, color='r', label='Measured data $y$')

# Plot the vector Ax (projection onto the line)
plt.quiver(0, 0, Ax[0], Ax[1], angles='xy', scale_units='xy', scale=1, color='b', label='Projection $A x$')

# Plot the line spanned by A
line_x = np.linspace(-2, 2, 100)
line_y = (A[1] / A[0]) * line_x
plt.plot(line_x, line_y, 'g--', label='Line spanned by $A$', linewidth=1)

# Set the axes limits
plt.xlim(-1, 5)
plt.ylim(-1, 5)

# Add labels and title
plt.xlabel('$y_1$')
plt.ylabel('$y_2$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.title('Geometrical Interpretation of Least-Squares Solution')
plt.legend()

# Show the plot
plt.show()
