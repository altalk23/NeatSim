import pygame as pg

from screen.colors import Colors


class Screen:

    def __init__(self):
        pg.init()

    '''
    Sets the framerate of the screen
    '''
    def setFramerate(self, framerate):
        self.clock = pg.time.Clock()
        self.framerate = framerate

    '''
    Sets the window size of the screen
    '''
    def setWindow(self, width, height):
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width, height))

    '''
    Sets the font of the screen
    '''
    def setFont(self, font, size):
        self.font = pg.font.Font(font, size)

    '''
    This method is called to start the screen
    '''
    def start(self):
        self.running = True

        while self.running:
            self.screen.fill(Colors.white)
            self.deltatime = self.clock.tick(self.framerate)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            pg.display.update()
        pg.quit()
