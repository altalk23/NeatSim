import pygame as pg

from utilities.size import Size
from utilities.colors import Colors
from utilities.coordinate import Coordinate
from utilities.boundingbox import BoundingBox


class BaseTile(pg.sprite.DirtySprite):

    def __init__(self, color: tuple, coordinate: Coordinate):
        self.color = color
        self.coordinate = coordinate
        pg.sprite.DirtySprite.__init__(self)
        self.id = 0

    def setBoundingBox(self, boundingBox: BoundingBox):
        self.image = pg.Surface(boundingBox.size.tuple())
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = boundingBox.coordinate.tuple()
        self.dirty = 1
