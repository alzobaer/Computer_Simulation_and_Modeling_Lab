import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

a = [1.0]     # 1 mole per liter
b = [0.5]     # 0.5 mole per liter
c = [0.0]     # 0 mole per liter

k1, k2 = 0.05, 0.05

total_time = 100    # 100 sec
steps = 500
dt = total_time / steps

time_values = [0]

for step in range(1, steps + 1):
    a_new = a[-1] + (k2 * c[-1] - k1 * a[-1] * b[-1]) * dt
    b_new = b[-1] + (k2 * c[-1] - k1 * a[-1] * b[-1]) * dt
    c_new = c[-1] + (2 * k1 * a[-1] * b[-1] - 2 * k2 * c[-1]) * dt

    a.append(a_new)
    b.append(b_new)
    c.append(c_new)
    time_values.append(step * dt)

fig, ax = plt.subplots()
ax.set_xlim(0, total_time)
ax.set_ylim(0, max(a + b + c))
ax.set_xlabel('Time')
ax.set_ylabel('Concentration')
ax.set_title('Concentration vs. Time')
ax.grid()

line_a, = ax.plot([], [], label='A', c='blue')
line_b, = ax.plot([], [], label='B', c='red')
line_c, = ax.plot([], [], label='C', c='green')


def update(frame):
    line_a.set_data(time_values[:frame], a[:frame])
    line_b.set_data(time_values[:frame], b[:frame])
    line_c.set_data(time_values[:frame], c[:frame])
    return line_a, line_b, line_c


ani = FuncAnimation(fig, update, frames=len(time_values), blit=True)
plt.legend()
plt.show()
