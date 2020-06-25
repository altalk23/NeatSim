import pygame as pg

from utilities.size import Size
from utilities.colors import Colors
from utilities.coordinate import Coordinate


class BaseTile(pg.sprite.DirtySprite):

    def __init__(self, color: tuple, size: Size, coordinate: Coordinate):
        pg.sprite.DirtySprite.__init__(self)

        self.id = 0

        self.image = pg.Surface(size.tuple())
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (coordinate.x * 60, coordinate.y * 60)
