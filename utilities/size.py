from math import ceil

from utilities.orientation import Orientation

class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get(self):
        return (self.width, self.height)


    def __truediv__(self, other):
        return Size(self.width / other.width, self.height / other.height)

    def ceil(self):
        return Size(ceil(self.width), ceil(self.height))

    def __eq__(self, other):
        return self.get() == other.get()

    def blank():
        return Size(
            0,
            0
        )

    def __mul__(self, other):
        return (self.width * other, self.height * other)
