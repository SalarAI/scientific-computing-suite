import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 100)
y = lambda x: x**2
x = np.random.random(len(t))
plt.plot(t, y(t), 'r--')
plt.scatter(t, x)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
