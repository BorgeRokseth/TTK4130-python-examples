import matplotlib.pyplot as plt
import math

def dot_x(x):
    if x < 0:
        return math.sqrt(-x)
    else:
        return math.sqrt(x)
time = 0
x = 0.1 # try to change initial condition to 0 and the dynamics will change unexpectedly
dt = 0.1

data = [x]
times = [time]

while time < 10:
    x = x + dot_x(x) * dt
    time = time + dt

    data.append(x)
    times.append(time)
fig, ax = plt.subplots()
ax.plot(times, data, lw=3)

plt.xlabel("time(s)")
plt.ylabel("x(t)")
plt.show()