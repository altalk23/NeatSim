import pygame as pg
from pygame import gfxdraw
from math import degrees, ceil
from os import path

from utilities.colors import Colors


class Sim(pg.sprite.DirtySprite):

    def __init__(self, simsystem, id):
        pg.sprite.DirtySprite.__init__(self)

        self.simsystem = simsystem
        self.id = id
        self.delta = simsystem.tilesystem.delta


        #self.texture = pg.Surface((256, 256))
        #pg.draw.circle(self.texture, Colors.black, (128, 128), 128)
        #pg.draw.polygon(self.texture, Colors.white, [(128, 32), (64, 96), (192, 96)])

    def draw(self):
        self.image = pg.Surface((self.rect.width, self.rect.height))
        pg.draw.circle(self.image, Colors.black,
            (self.rect.width/2, self.rect.height/2),
            self.rect.width/2
        )
        #gfxdraw.aacircle(self.image, self.rect.width//2, self.rect.height//2, self.rect.width//2, Colors.black)
        #gfxdraw.filled_circle(self.image, self.rect.width//2, self.rect.height//2, self.rect.width//2, Colors.black)

        pg.draw.polygon(self.image, Colors.white, [
            (4*self.rect.width/8, 2*self.rect.height/8),
            (2*self.rect.width/8, 4*self.rect.height/8),
            (6*self.rect.width/8, 4*self.rect.height/8)
        ])
        self.image = pg.transform.rotozoom(self.image, self.r, 1.0)
        self.dirty = 1

    def setPosition(self, x, y):
        self.x = x
        self.y = y

        drawX = x * self.simsystem.tilesystem.tileWidth
        drawY = y * self.simsystem.tilesystem.tileHeight
        drawWidth = 4
        drawHeight = 4
        self.baseRect = pg.Rect(drawX, drawY, drawWidth, drawHeight)
        self.rect = self.delta.delta(self.baseRect)

    def setRotation(self, r):
        self.r = r

    def update(self):
        self.rect = self.delta.delta(self.baseRect)
        self.draw()
    '''
    def updatePosition(self, position):
        self.position = position
        self.visible = position.bb.colliding(self.tilesystem.windowBB)

        self.rect = self.image.get_rect()
        self.rect.center = position.bb.getCenter()
        self.dirty = 1


    def updateScale(self, position):
        size = position.bb.getSize()
        size = (ceil(size[0]), ceil(size[1]))
        self.scaled = pg.transform.smoothscale(self.texture, size)
        self.updateRotation(position)
        self.updatePosition(position)

    def updateRotation(self, position):
        self.image = pg.transform.rotate(self.scaled, degrees(position.angle))
        self.updatePosition(position)
    '''
