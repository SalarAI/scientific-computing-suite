import matplotlib.pyplot as plt

x = [i for i in range(0, 20, 2)]
y = [i for i in range(0, 30, 3)]
plt.plot(x, y, 'ro-')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show(block=True)
