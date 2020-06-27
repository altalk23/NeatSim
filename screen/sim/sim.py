import pygame as pg
from math import degrees, ceil
from os import path

from utilities.position import Position

class Sim(pg.sprite.DirtySprite):
    position = Position.blank()

    def __init__(self, tilesystem, simsystem, id):
        pg.sprite.DirtySprite.__init__(self)

        self.simsystem = simsystem
        self.tilesystem = tilesystem
        self.id = id

        self.texture = pg.image.load(path.join('resources', 'sim.png'))
        self.rectangle = self.texture.get_rect()

    def updatePosition(self, position):
        if self.position != position:
            self.image = pg.transform.rotate(self.scaled, degrees(position.angle))

            self.rect = self.image.get_rect()
            self.rect.topleft = position.bb.getCoordinate()
            dirty = 1

    def updateScale(self, position):
        size = position.bb.getSize()
        size = (ceil(size[0]), ceil(size[1]))
        self.scaled = pg.transform.scale(self.texture, size)
        self.updatePosition(position)
