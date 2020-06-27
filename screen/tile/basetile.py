import pygame as pg

from utilities.size import Size
from utilities.colors import Colors
from utilities.coordinate import Coordinate
from utilities.boundingbox import BoundingBox


class BaseTile(pg.sprite.DirtySprite):

    def __init__(self, color: tuple, coordinate: Coordinate, system):
        pg.sprite.DirtySprite.__init__(self)

        self.color = color
        self.coordinate = coordinate
        self.boundingBox = None

        self.system = system
        self.id = 0


        self.visible = 1
        self.removed = 0

    def updateBoundingBox(self, boundingBox: BoundingBox):
        self.boundingBox = boundingBox
        self.visible = boundingBox.colliding(BoundingBox(Coordinate(0, 0), self.system.windowSize))

        if self.visible:
            self.image = pg.Surface(boundingBox.getSize())
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            self.rect.topleft = boundingBox.getCoordinate()
            self.dirty = 1
            self.removed = 0

        elif not self.removed:
            self.dirty = 1
            self.removed = 1
