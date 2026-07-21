import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def parameter(A = 16, B = 13, C = 5, D = 2):
    t = np.linspace(0, 2 * np.pi, 500)
    x = A * np.sin(t) ** 3
    y = B * np.cos(t) - C * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return t, x, y


def setup_axis(axis):
    axis.set_xlim(-20, 20)
    axis.set_ylim(-20, 20)
    axis.axis("off")
    return axis


def setup_plot(axis):
    (line,) = axis.plot([], [], color="red", linewidth=4)
    return line


def animation(i, x, y, line):
    scale = 1 + 0.25 * np.sin(i * (1 / 2))
    pulse = (np.sin(i * (1 / 2)) + 1) / 2
    color = (1, pulse, pulse)
    line.set_data(scale * x, scale * y)
    line.set_color(color)
    line.set_linewidth(4)
    return (line,)


if __name__ == "__main__":
    fig, axis = plt.subplots()
    fig.patch.set_color("black")
    axis = setup_axis(axis)
    t, x, y = parameter()
    line = setup_plot(axis)

    def init():
        line.set_data([], [])
        return (line,)

    ani = FuncAnimation(
        fig=fig,
        func=animation,
        fargs=(x, y, line),
        init_func=init,
        frames=300,
        interval=30,
        blit=True,
    )

    plt.show()

