import pygame as pg

from utilities.colors import Colors
from utilities.size import Size
from screen.tile.tilesystem import TileSystem
from screen.sim.simsystem import SimSystem
from screen.tile.delta import Delta
from screen.panel.panel import Panel



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
    def setWindow(self, width, height):
        # Fullscreen
        if width == 0 and height == 0:
            self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
            info = pg.display.Info()
            self.width = info.current_w
            self.height = info.current_h

        # Windowed
        else:
            self.screen = pg.display.set_mode((width, height))
            self.width = width
            self.height = height


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

        surface = pg.Surface((self.width, self.height), pg.SRCALPHA)
        surface.fill(Colors.darkGray, pg.Rect(self.height, 0, self.width-self.height, self.height))
        surface = surface.convert_alpha()
        group = pg.sprite.Group()
        group.clear(self.screen, surface)

        # Delta
        delta = Delta(self.height, self.height)

        # Tilesystem
        tilesystem = TileSystem(self.screen, delta)
        tilesystem.setSize(self.height, self.height)
        tilesystem.generateTiles(100, 100)

        # Simsystem
        simsystem = SimSystem(group, tilesystem)
        simsystem.generateSims(50)

        # Simsystem
        #simsystem = SimSystem(tilesystem, allsprites)
        #simsystem.generateSims(50)

        #panel.bindSimSystem(simsystem)
        panelSurface = pg.Surface((self.width-self.height, self.height))
        panelSurface.fill(Colors.darkGray)
        panel = Panel(tilesystem, simsystem, self)
        panel.setSize(self.width - self.height, self.height)

        # Main loop
        while running:
            a = self.clock.tick(self.framerate)
            if a > 36:
                print(a)


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    #if not simsystem.selectSim(event.pos):
                    #
                    if event.button == 1:
                        #tilesystem.randomColor()
                        if simsystem.selectSim(event.pos):
                            panel.dirty = 1
                        else:
                            self.down = event.pos
                    elif event.button == 4:
                        delta.zoomOut()
                    elif event.button == 5:
                        delta.zoomIn()

                    pass

                if event.type == pg.MOUSEMOTION:
                    if self.down is not None:
                        delta.move(event.pos[0] - self.down[0], event.pos[1] - self.down[1])
                        self.down = event.pos
                    #
                    #    tilesystem.move()
                    #    simsystem.updateSims()
                    #    self.down = event.pos

                if event.type == pg.MOUSEBUTTONUP:
                    self.down = None

            if delta.dirty:
                delta.dirty = 0
                tilesystem.deltaChange()
                #simsystem.deltaChange()
            #
            rect = tilesystem.drawTiles()

            simsystem.move()
            group.update()
            group.draw(self.screen)
            rect += [sprite.rect for sprite in group.sprites()]
            self.screen.blit(surface, (0, 0))
            pg.display.update()
        pg.quit()
