
import numpy as np
from enum import Enum

from src.objects.ball import Ball
from src.physics.dynamics import Newton


class Events(Enum):
    REFLECTION = "reflection"
    MOVE = "move"
    COLLISION_X = "collision_x"
    END = "end"


class EventGenerator:
    @staticmethod
    def next_event(objectL: Ball, objectR: Ball):
        rL = objectL.radius
        dmax = Newton.max_distance(objectL, objectR)
        xL, xR = objectL.coordinates.x, objectR.coordinates.x
        vxL, vxR = objectL.velocity.x, objectR.velocity.x

        if vxL < 0 and vxR > 0:
            # <-- ->  < 0 REFLECTION
            # <- -->  > 0 REFLECTION
            return Events.REFLECTION, (xL-rL) / np.abs(vxL)
        elif vxL > 0 and vxR < 0:
            # -> <--  < 0 COLLISION
            # --> <-  > 0 COLLISION
            return Events.COLLISION_X, (xR - xL - dmax) / (vxL + np.abs(vxR))
        elif vxL > 0 and vxR > 0:
            # -> -->  > 0 END
            if vxR >= vxL:
                return Events.END, np.inf
            # --> ->  > 0 COLLISION
            if vxR < vxL:
                return Events.COLLISION_X, (xR - xL - dmax) / (vxL - vxR)
        elif vxL <= 0 and vxR < 0:
            # <-- <-  > 0 REF
            if np.abs(vxL) >= np.abs(vxR):
                return Events.REFLECTION, (xL - rL) / np.abs(vxL)

            t_reflection = (xL - rL) / np.abs(vxL) if vxL != 0 else np.inf
            t_collision = (xR - xL - dmax) / (np.abs(vxR) - np.abs(vxL))
            # <- <--  < 0 ?
            if t_reflection < t_collision:
                return Events.REFLECTION, t_reflection
            else:
                return Events.COLLISION_X, t_collision
        elif vxL < 0 and vxR == 0:
            return Events.REFLECTION, (xL - rL) / np.abs(vxL)
        elif vxL > 0 and vxR == 0:
            return Events.COLLISION_X, (xR - xL - dmax) / vxL

        raise ValueError("Impossible event")

    @staticmethod
    def propagate(objectL: Ball, objectR: Ball, dt: float):
        T = dt
        nb_collisions = 0

        while T > 0:
            event, ti = EventGenerator.next_event(objectL, objectR)
            assert ti >= 0, "Wrong time value"

            Newton.move(objectL, ti)
            Newton.move(objectR, ti)

            if event == Events.COLLISION_X:
                Newton.collision_x(objectL, objectR)
                nb_collisions += 1
            elif event == Events.REFLECTION:
                Newton.reflection(objectL)
                nb_collisions += 1
            elif event == Events.END:
                pass
            else:
                raise NotImplementedError(f"Unknown event type {event.name}")

            T = T - ti

        next_event, _ = EventGenerator.next_event(objectL, objectR)
        return nb_collisions, next_event
