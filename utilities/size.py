from math import ceil

from utilities.orientation import Orientation

class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def tuple(self):
        return (self.width, self.height)


    def __truediv__(self, other):
        return Size(self.width / other.width, self.height / other.height)

    def ceil(self):
        return Size(ceil(self.width), ceil(self.height))
