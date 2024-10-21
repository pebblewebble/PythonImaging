import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)
line, = ax.plot(x, np.sin(x))

# Initialize the moving circle
circle = plt.Circle((0, np.sin(0)), 0.2, fc='r')  # Circle starts at (0, sin(0))

# Initialization function
def init():
    ax.set_xlim(0, 2 * np.pi)  # Same x-limits as the sine wave
    ax.set_ylim(-1.5, 1.5)     # Y-limits to accommodate the sine wave
    ax.add_artist(circle)
    return circle, line

# Animation function for the line and circle
def animate(i):
    # Update the line with the sine wave motion
    line.set_ydata(np.sin(x + i / 10.0))

    # Find the current x position for the circle
    current_x = x[i % len(x)]
    # Set the circle's center to follow the sine wave
    current_y = np.sin(current_x + i / 10.0)
    circle.set_center((current_x, current_y))

    return circle, line

# Create the animation
animation = FuncAnimation(fig, animate, init_func=init, frames=len(x), interval=50, blit=True)

# Show the plot
plt.show()
