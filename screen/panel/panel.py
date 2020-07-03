import pygame as pg

from utilities.colors import Colors

class Panel:
    items = []

    def __init__(self, tilesystem, simsystem, screen):
        self.tilesystem = tilesystem
        self.simsystem = simsystem
        self.screen = tilesystem.screen
        self.font = screen.font

    def setSize(self, width, height):
        self.rect = pg.Rect(height, 0, width, height)
        print(self.rect)
        self.surface = pg.Surface((width, height))

    def drawContent(self):
        self.surface.fill(Colors.black)
        if self.simsystem.selected is not None:
            selectedText = self.font.render(f'Selected: {self.simsystem.selected.id}', True, Colors.white)
        self.screen.blit(self.surface, (self.rect.x, self.rect.y))
        return self.rect
        return None
