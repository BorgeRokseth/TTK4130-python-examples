import matplotlib.pyplot as plt

def dot_x(x):
    return x ** 2
time = 0
x = 0.18
dt = 1

data = [x]
times = [time]
sim_time = 9

while time < sim_time: # try somulating longer (e.g. 20 sec)
    x = x + dot_x(x) * dt
    time = time + dt

    data.append(x)
    times.append(time)


fig, ax = plt.subplots()
ax.plot(times, data, lw=3)
plt.xlabel("time(s)")
plt.ylabel("x(t)")
plt.show()