import pygame as pg

class SelectedSim(pg.sprite.Sprite):
    def __init__(self, simsystem, id):
        pg.sprite.Sprite.__init__(self)

    def update(self):
        
