from utilities.size import Size
from utilities.coordinate import Coordinate

class BoundingBox:
    def __init__(self, coordinate: Coordinate, size: Size):
        self.coordinate = coordinate
        self.size = size

    def tuple(self):
        return (self.coordinate.tuple, self.size.tuple)
