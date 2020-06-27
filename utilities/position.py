from utilities.boundingbox import BoundingBox

class Position:
    def __init__(self, bb: BoundingBox, angle: float):
        self.bb = bb
        self.angle = angle

    def get(self):
        return (self.bb.get(), self.angle)

    def __eq__(self, other):
        return self.get() == other.get()

    def blank():
        return Position(
            BoundingBox.blank(),
            0
        )
