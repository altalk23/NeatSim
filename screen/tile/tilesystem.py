import pygame as pg
from random import randint

from screen.tile.tile import Tile

class TileSystem:

    def __init__(self, screen, delta):
        self.screen = screen
        self.delta = delta

    '''
    Sets the window size of the system
    '''
    def setSize(self, width: int, height: int) -> None:
        self.rect = pg.Rect(0, 0, width, height)
        self.surface = pg.Surface((width, height))



    '''
    Initializes the tiles in the system
    '''
    def generateTiles(self, width: int, height: int) -> None:
        self.systemWidth = width
        self.systemHeight = height

        self.tiles = []

        self.tileWidth = self.rect.width / self.systemWidth
        self.tileHeight = self.rect.height / self.systemHeight

        for x in range(width):
            self.tiles.append([])
            for y in range(height):

                drawX = x * self.tileWidth
                drawY = y * self.tileHeight
                drawWidth = self.tileWidth
                drawHeight = self.tileHeight
                drawRect = pg.Rect(drawX, drawY, drawWidth, drawHeight)

                self.tiles[x].append(Tile((0, randint(111, 143), 0), drawRect))


    '''
    Draws the tiles to the screen
    '''
    def drawTiles(self) -> list:
        rectList = []
        for column in self.tiles:
            for tile in column:
                if tile.dirty:
                    rect = self.delta.delta(tile.rect)
                    rectList.append(rect)
                    pg.draw.rect(self.surface, tile.color, rect)
                    tile.dirty = 0
        self.screen.blit(self.surface, (0, 0))
        return rectList


    '''
    Gives random color to %5 of tiles
    Debug function
    '''
    def randomColor(self) -> None:
        print(self.tiles[0][0])
        for column in self.tiles:
            for tile in column:
                if randint(0, 100) > 95:
                    tile.color = (0, randint(111, 143), 0)
                    tile.dirty = 1
        print(self.tiles[0][0])

    def deltaChange(self):
        for column in self.tiles:
            for tile in column:
                if self.rect.colliderect(self.delta.delta(tile.rect)):
                    tile.dirty = 1
