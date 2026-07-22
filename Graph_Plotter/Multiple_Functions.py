import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 1000)
x1 = np.sin(t)
x2 = np.cos(t)
x3 = np.tan(t)

fig, axis = plt.subplots(1, 3, figsize=(8, 6))
axis[0].plot(t, x1)
axis[1].plot(t, x2)
axis[2].plot(t, x3)
fig.tight_layout()
plt.show(block=True)
