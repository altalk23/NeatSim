import pygame as pg

from utilities.colors import Colors
from utilities.size import Size
from screen.tile.tilesystem import TileSystem


class Screen:

    '''
    Screen initializer
    '''
    def __init__(self):
        pg.init()

    '''
    Sets the framerate of the screen
    '''
    def setFramerate(self, framerate: int):
        self.clock = pg.time.Clock()
        self.framerate = framerate

    '''
    Sets the window size of the screen
    '''
    def setWindow(self, size: Size):
        # Fullscreen
        if size is None:
            self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
            info = pg.display.Info()
            self.size = Size(info.current_w, info.current_h)

        # Windowed
        else:
            self.screen = pg.display.set_mode(size.tuple())
            self.size = size


    '''
    Sets the font of the screen
    '''
    def setFont(self, font: str, size: int):
        self.font = pg.font.Font(font, size)

    '''
    This method is called to start the screen
    '''
    def start(self):
        running = True

        # Background
        background = pg.Surface(self.size.tuple())
        background = background.convert()
        background.fill(Colors.white)


        # Tilesystem
        tilesystem = TileSystem()
        if self.size.width >= self.size.height:
            tilesystem.setSize(Size(self.size.height, self.size.height))
        else:
            tilesystem.setSize(Size(self.size.width, self.size.width))
        tilesystem.generateTiles(Size(32, 32))


        # All sprites
        allsprites = pg.sprite.LayeredDirty(tilesystem.tiles)
        allsprites.clear(self.screen, background)


        # Main loop
        while running:
            self.clock.tick(self.framerate)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_i:
                        tilesystem.zoomIn()

            allsprites.update()

            rect = allsprites.draw(self.screen)
            pg.display.update(rect)
        pg.quit()
