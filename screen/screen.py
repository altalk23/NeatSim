import pygame as pg

from utilities.colors import Colors
from utilities.size import Size
from screen.tile.tilesystem import TileSystem
from screen.sim.simsystem import SimSystem



class Screen:
    down = None

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
            self.screen = pg.display.set_mode(size.get())
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
        simSurface = pg.Surface(self.size.get(), pg.SRCALPHA)
        simSurface = simSurface.convert_alpha()

        # Tilesystem
        tilesystem = TileSystem(self.screen)
        tilesystem.setSize(self.size.height, self.size.height)
        tilesystem.generateTiles(100, 100)

        # Simsystem
        simGroup = pg.sprite.LayeredDirty()
        simGroup.clear(self.screen, simSurface)
        simsystem = SimSystem(simGroup, tilesystem)
        simsystem.generateSims(50)

        # Simsystem
        #simsystem = SimSystem(tilesystem, allsprites)
        #simsystem.generateSims(50)

        #panel.bindSimSystem(simsystem)

        # Main loop
        while running:
            self.clock.tick(self.framerate)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    #if not simsystem.selectSim(event.pos):
                    #    self.down = event.pos
                    tilesystem.randomColor()
                    simGroup.update()
                    pass

                if event.type == pg.MOUSEMOTION:
                    #if self.down is not None:
                    #    tilesystem.move(event.pos[0] - self.down[0], event.pos[1] - self.down[1])
                    #    simsystem.updateSims()
                    #    self.down = event.pos
                    pass

                if event.type == pg.MOUSEBUTTONUP:
                    #self.down = None
                    pass
            #
            rect = tilesystem.drawTiles()
            rect += simGroup.draw(self.screen)
            pg.display.update(rect)
        pg.quit()
