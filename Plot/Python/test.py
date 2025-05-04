import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 200)
x = 5 * np.cos(t * np.pi)
y = 5 * np.sin(t * np.pi)

plt.figure(figsize=(8,6))
plt.plot(x, y, label=f'Curva Circular', color='red')
plt.scatter(5 * np.cos(3 * np.pi), 5 * np.sin(4 * np.pi), color='black', s=150, zorder=10)
plt.quiver(0, 0, 5 * np.cos(3 * np.pi), 5 * np.sin(4 * np.pi), scale = 25, zorder = 6)
plt.quiver(5 * np.cos(3 * np.pi), 5 * np.sin(4 * np.pi), -5 * np.sin(3 * np.pi), 5 * np.cos(4 * np.pi), color = 'blue', scale = 25, zorder = 6)
plt.quiver(5 * np.cos(3 * np.pi), 5 * np.sin(4 * np.pi), -5 * np.cos(3 * np.pi), -5 * np.sin(4 * np.pi), color = 'red', scale = 25, zorder = 6)
plt.title('Trajetória')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal')
plt.legend()
plt.grid(True)
plt.show()