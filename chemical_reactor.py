# Import necessary libraries
import matplotlib.pyplot as plt

# Define initial concentrations and parameters
a = [1.0]     # Initial concentration of A: 1 mole per liter
b = [0.5]     # Initial concentration of B: 0.5 mole per liter
c = [0.0]     # Initial concentration of C: 0 mole per liter

k1, k2 = 0.05, 0.05  # Rate constants for the chemical reaction

total_time = 100    # Total time for the simulation in seconds
steps = 500         # Number of time steps
dt = total_time / steps  # Time step size

time_values = [0]  # Initialize a list to store time values

# Perform the simulation
for step in range(1, steps + 1):
    # Calculate new concentrations using the rate equations
    a_new = a[-1] + (k2 * c[-1] - k1 * a[-1] * b[-1]) * dt
    b_new = b[-1] + (k2 * c[-1] - k1 * a[-1] * b[-1]) * dt
    c_new = c[-1] + (2 * k1 * a[-1] * b[-1] - 2 * k2 * c[-1]) * dt

    # Append the new concentrations and time values to the respective lists
    a.append(a_new)
    b.append(b_new)
    c.append(c_new)
    time_values.append(step * dt)

# Create a plot to visualize the concentration changes over time
plt.plot(time_values, a, label='A')
plt.plot(time_values, b, label='B')
plt.plot(time_values, c, label='C')

# Set plot labels, legend, and title
plt.xlabel('Time (s)')
plt.ylabel('Concentration (moles per liter)')
plt.legend()
plt.title('Concentration vs. Time')
plt.grid()

# Display the plot
plt.show()
