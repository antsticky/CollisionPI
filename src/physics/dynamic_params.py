class Velocity:
    def __init__(self, x: float):
        self.x = x

    def __available_directions(self):
        return [attr for attr in dir(self) if "__" not in attr]

    def __iter__(self):
        yield from self.__available_directions()


class Coordinates:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
