
import numpy as np

from src.objects.ball import Ball


class Newton:
    @staticmethod
    def max_distance(object1: Ball, object2: Ball):
        if all([isinstance(object1, Ball), isinstance(object2, Ball)]):
            R = object1.radius if object1.radius > object2.radius else object2.radius
            r = object1.radius if object1.radius < object2.radius else object2.radius

            if r == R:
                return 2 * r

            alpha = np.arcsin((R - r) / (R + r))
            return (R - r) / np.tan(alpha)

        raise NotImplementedError("It works only for balls")

    @staticmethod
    def collision_x(object1: Ball, object2: Ball):
        m1, u1 = object1.mass, object1.velocity.x
        m2, u2 = object2.mass, object2.velocity.x
        m_total = m1 + m2

        v1 = (m1 - m2) / m_total * u1 + 2 * m2 / m_total * u2
        v2 = 2 * m1 / m_total * u1 + (m2 - m1) / m_total * u2

        object1.velocity.x = v1
        object2.velocity.x = v2

    @staticmethod
    def reflection(object: Ball, direction="x"):
        setattr(object.velocity, direction, -
                getattr(object.velocity, direction))

    @staticmethod
    def move(object: Ball, dt: float):
        for i in object.velocity:
            setattr(object.coordinates, i, getattr(
                object.coordinates, i) + dt * getattr(object.velocity, i))
