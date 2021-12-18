from src.physics.dynamics import Newton

from src.collision.events import Events, EventGenerator


def get_nb_collisions(ball1, ball2):
    nb_collisions = 0
    next_event = Events.COLLISION_X
    while next_event != Events.END:
        nb_collisions_i, next_event = EventGenerator.propagate(ball1, ball2, 2)
        nb_collisions += nb_collisions_i
    return nb_collisions
