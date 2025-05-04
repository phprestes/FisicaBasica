import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

t = np.linspace(0, 2, 200)
x = 5 * np.cos(t * np.pi)
y = 5 * np.sin(t * np.pi)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    return line,

ani = animation.FuncAnimation(fig, update, len(t), interval=100, fargs=[x, y, line], blit=True)
ani.save("aaa.mp4", writer=animation.FFMpegWriter(fps=60, bitrate=5000, codec='h264'), dpi=100)
