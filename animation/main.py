
from time import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib.patches as patches

from src.objects.ball import Ball
from src.collision.events import EventGenerator
from src.physics.dynamic_params import Coordinates, Velocity

digits = 3
ground_height = 0.5

r = 0.5
R = 0.75
m1, m2 = 1.0, np.power(100, digits-1)
ball1 = Ball(coordinates=Coordinates(x=3, y=ground_height + r),
             velocity=Velocity(x=0), mass=m1, radius=r)
ball2 = Ball(coordinates=Coordinates(x=8, y=ground_height + R),
             velocity=Velocity(x=-1), mass=m2, radius=R)
inspect_dict = {"nb_collisions": 0}


################################################################
fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

wall_width = 0.5
wall_height = 8
ax = plt.axes(xlim=(-wall_width, 10), ylim=(0, 10))
circle1 = plt.Circle((ball1.coordinates.x, ball1.coordinates.y), r, fc="b")
circle2 = plt.Circle((ball2.coordinates.x, ball2.coordinates.y), R, fc="r")
text_box = ax.text(7, 9, f" ", ha='center', va='center',
                   fontsize=20, color="Red")


def init():
    rect_wall = patches.Rectangle((0, ground_height), -wall_width,
                                  wall_height, linewidth=1, edgecolor='black', facecolor='black')
    ax.add_patch(rect_wall)

    rect_ground = patches.Rectangle(
        (-wall_width, 0), 10+wall_width, ground_height, linewidth=1, edgecolor='green', facecolor='green')
    ax.add_patch(rect_ground)

    ax.add_patch(circle1)
    ax.add_patch(circle2)

    return (circle1, circle2, text_box)


def animate(i):
    text_box.set_text(f'collisions = {inspect_dict["nb_collisions"]}')

    nb_collisions_i, _ = EventGenerator.propagate(
        ball1, ball2, 0.01)
    circle1.center = (ball1.coordinates.x, ball1.coordinates.y)
    circle2.center = (ball2.coordinates.x, ball2.coordinates.y)

    inspect_dict["nb_collisions"] += nb_collisions_i

    return (circle1, circle2, text_box)


if __name__ == '__main__':
    dt = 1./30
    t0 = time()
    animate(0)
    t1 = time()
    interval = 1000 * dt - (t1 - t0)
    anim = animation.FuncAnimation(
        fig, animate, init_func=init, frames=360, interval=interval, blit=True)
    plt.show()
