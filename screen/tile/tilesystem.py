import pygame as pg
from random import randint

from utilities.size import Size
from screen.tile.basetile import BaseTile
from utilities.coordinate import Coordinate
from utilities.boundingbox import BoundingBox

class TileSystem:
    dx = 0
    dy = 0
    dr = 0
    dz = 0
    curve = lambda self, x: (x+1)**0.75

    '''
    Initializes the tile system
    '''
    def __init__(self):
        pass

    '''
    Sets the window size of the system
    '''
    def setSize(self, size: Size):
        self.windowSize = size
        self.currentSize = size

    '''
    Initializes the tiles in the system
    '''
    def generateTiles(self, size: Size):
        self.systemSize = size
        self.tiles = []
        for x in range(size.width):
            for y in range(size.height):
                self.tiles.append(
                    BaseTile(
                        (randint(111, 143), 0, 0),
                        Coordinate(x, y),
                        self
                    )
                )
        self.updateTiles()

    def updateTiles(self):
        self.tileSize = self.currentSize / self.systemSize
        for tile in self.tiles:
            if tile.boundingBox is None:
                tile.updateBoundingBox(
                    BoundingBox(
                        Coordinate(
                            tile.coordinate.x * self.tileSize.width,
                            tile.coordinate.y * self.tileSize.height
                        ),
                        self.tileSize.ceil()
                    )
                )
            else:
                boundingBox = tile.boundingBox
                boundingBox.align(self.curve(self.dz), self.dx, self.dy)
                tile.updateBoundingBox(
                    boundingBox
                )


    '''
    Zooms in
    '''
    def zoomIn(self):
        if self.dz < 20:
            pdz = self.curve(self.dz)
            self.dz += 1
            self.changeZoom(pdz)

    '''
    Zooms out
    '''
    def zoomOut(self):
        if self.dz > 0:
            pdz = self.curve(self.dz)
            self.dz -= 1
            self.changeZoom(pdz)

    def limitMove(self):
        self.dx = max(min(self.dx, 0), - self.currentSize.width + self.windowSize.width)
        self.dy = max(min(self.dy, 0), - self.currentSize.height + self.windowSize.height)

    '''
    Changes zoom
    '''
    def changeZoom(self, pdz):
        dz = self.curve(self.dz)

        self.dx -= self.windowSize.width * (dz - pdz) / 2
        self.dy -= self.windowSize.height * (dz - pdz) / 2

        self.currentSize = Size(
            self.windowSize.width * dz,
            self.windowSize.height * dz,
        )

        self.limitMove()
        self.updateTiles()

    def move(self, dx, dy):
        self.dx += dx
        self.dy += dy
        self.limitMove()
        self.updateTiles()
