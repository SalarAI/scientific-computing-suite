import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')
ax.set_title("Shanks Haki")
ax.scatter([0], [0], [0], color='red', s=500, label='Shanks')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.tan(np.sqrt(x**2 + y**2))

surface = ax.plot_surface(x, y, z)
fig.colorbar(surface)

plt.show()
