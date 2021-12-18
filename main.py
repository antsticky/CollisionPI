import numpy as np
from enum import Enum

from src.physics.dynamic_params import Coordinates, Velocity
from src.objects.ball import Ball

from src.collision.calculator import get_nb_collisions


def main():
    #digits = 6
    digits = 6

    r1, r2 = 0.3, 0.6
    m1, m2 = 1.0, np.power(100, digits-1)
    v1, v2 = 0, -1.0
    x1, x2 = 2, 3

    ball1 = Ball(coordinates=Coordinates(x=x1, y=r1),
                 velocity=Velocity(x=v1), mass=m1, radius=r1)
    ball2 = Ball(coordinates=Coordinates(x=x2, y=r2),
                 velocity=Velocity(x=v2), mass=m2, radius=r2)

    nb_collisions = get_nb_collisions(ball1, ball2)

    pi_simmulation = nb_collisions/np.power(10, digits-1)
    pi_approx = round(np.pi, digits-1)

    print(pi_simmulation, pi_approx)


if __name__ == "__main__":
    main()
