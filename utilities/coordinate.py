class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

    def __eq__(self, other):
        return self.get() == other.get()

    def blank():
        return Coordinate(
            0,
            0
        )
