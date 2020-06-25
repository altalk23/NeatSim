import pygame as pg
from random import randint

from utilities.size import Size
from screen.tile.basetile import BaseTile
from utilities.coordinate import Coordinate

class TileSystem:
    dx = 0
    dy = 0
    dr = 0
    dz = 1

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

    '''
    Initializes the tiles in the system
    '''
    def generateTiles(self, size: Size):
        self.systemSize = size

        self.tiles = []
        for x in range(size.width):
            for y in range(size.height):
                self.tiles.append(BaseTile((randint(111, 143), 0, 0), self.windowSize / size, Coordinate(x, y)))
        pass

    '''
    Zooms in
    '''
    def zoomIn(self):
        self.dz += 1
