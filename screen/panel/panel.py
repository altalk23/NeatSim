from screen.panel.stats import Stats
from utilities.boundingbox import BoundingBox
from utilities.orientation import Orientation

class Panel:
    items = []

    def bindSimSystem(self, simsystem):
        self.simsystem = simsystem
        self.items.append(Stats())

    def setBoundingBox(self, boundingBox):
        self.size = boundingBox.getSize()
        self.coordinate = boundingBox.getCoordinate()
        if self.size.width >= self.size.height:
            self.orientation = Orientation.LANDSCAPE
        else:
            self.orientation = Orientation.PORTRAIT
