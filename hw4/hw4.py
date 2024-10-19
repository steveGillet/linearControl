import numpy as np

# Define the vectors r4, q1, q2, q3
r4 = np.array([-10, 6, -11, -3, -23])
q1 = np.array([3, -1, 4, 0, 7])
q2 = np.array([-.72, 8.24, 6.04, -9, -.68])
q3 = np.array([0.128808757, -0.14084467, 0.086437648, 0.110109466, 0.288352715])

# Step 1: Calculate q1.q1
q1_dot_q1 = np.dot(q1, q1)

# Step 2: Calculate r4.q1
r4_dot_q1 = np.dot(r4, q1)

# Step 3: Calculate the first term to subtract
term1 = (r4_dot_q1 / q1_dot_q1) * q1

# Step 4: Calculate q2.q2
q2_dot_q2 = np.dot(q2, q2)

# Step 5: Calculate r4.q2
r4_dot_q2 = np.dot(r4, q2)

# Step 6: Calculate the second term to subtract
term2 = (r4_dot_q2 / q2_dot_q2) * q2

# Step 7: Calculate q3.q3
q3_dot_q3 = np.dot(q3, q3)

# Step 8: Calculate r4.q3
r4_dot_q3 = np.dot(r4, q3)

# Step 9: Calculate the third term to subtract
term3 = (r4_dot_q3 / q3_dot_q3) * q3

# Step 10: Calculate q4
q4 = r4 - term1 - term2 - term3
print(q4)
