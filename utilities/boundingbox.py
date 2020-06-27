from utilities.size import Size
from utilities.coordinate import Coordinate

class BoundingBox:
    dx = 0
    dy = 0
    dr = 0
    dz = 1

    def __init__(self, coordinate: Coordinate, size: Size):
        self.coordinate = coordinate
        self.size = size

    def align(self, dz: int, dx: int, dy: int):
        self.dz = dz
        self.dx = dx
        self.dy = dy

    def get(self):
        return (
            self.getCoordinate(),
            self.getSize()
        )

    def getCoordinate(self):
        c = self.coordinate.get()
        c = (c[0] * self.dz + self.dx, c[1] * self.dz + self.dy)
        return c

    def getSize(self):
        return self.size * self.dz



    def colliding(self, other):
        bb1 = self.get()
        bb2 = other.get()
        if (
            bb1[0][0] < bb2[0][0] + bb2[1][0] and
            bb1[0][0] + bb1[1][0] > bb2[0][0] and
            bb1[0][1] < bb2[0][1] + bb2[1][1] and
            bb1[0][1] + bb1[1][1] > bb2[0][1]
        ):
            return 1
        return 0

    def __eq__(self, other):
        return self.get() == other.get()

    def blank():
        return BoundingBox(
            Coordinate.blank(),
            Size.blank()
        )
