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
                        Coordinate(x, y)
                    )
                )
        self.updateTiles()

    def updateTiles(self):
        self.tileSize = self.currentSize / self.systemSize
        for tile in self.tiles:
            tile.setBoundingBox(
                BoundingBox(
                    Coordinate(
                        tile.coordinate.x * self.tileSize.width,
                        tile.coordinate.y * self.tileSize.height
                    ),
                    self.tileSize.ceil()
                )
            )




    '''
    Zooms in
    '''
    def zoomIn(self):
        curve = lambda x: self.windowSize.width/8/x
        if self.dz < 20:
            self.dz += 1
            self.dx += curve(self.dz)
            self.dy += curve(self.dz)
            self.currentSize = Size(
                self.windowSize.width - 2 * curve(self.dz),
                self.windowSize.height - 2 * curve(self.dz),
            )
            print(self.dz, self.dx, self.dy)
            self.updateTiles()
