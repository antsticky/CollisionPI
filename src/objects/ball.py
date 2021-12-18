from src.physics.dynamic_params import Coordinates, Velocity


class Ball:
    def __init__(self, coordinates: Coordinates, velocity: Velocity, radius: float, mass: float):
        self.coordinates = coordinates
        self.velocity = velocity
        self.radius = radius
        self.mass = mass
