import matplotlib.pyplot as plt

m = 2
k = 1
d = 0.5
y0 = 0  # the spring is unloaded when the mass is at position y=0
F = 0

# Initial states
y1 = 1  # initial position (1 meter over neutral position)
y2 = 0  # mass is at rest when simulation starts

# Simulation parameters
dt = 0.25  # we step 0.1 second ahead each iteration
t = 0  # initial time is 0
simulation_time = 10

# Prepare data storage
y1_data = [y1]
y2_data = [y2]
t_data = [t]

while t < simulation_time:
    # Update F
    F = 0  # in this special case, F is constantly 0
    
    # Calculate time-differentials
    dot_y1 = y2
    dot_y2 = 1/m * (-d*y2 - (y1-y0)*k + F)
    
    # Step ahead (using the euler method)
    y1 = y1 + dot_y1 * dt
    y2 = y2 + dot_y2 * dt
    t = t + dt
    
    # Store data
    y1_data.append(y1)
    y2_data.append(y2)
    t_data.append(t)



fig, position_ax = plt.subplots()

position_ax.plot(t_data, y1_data, "x")
plt.show()