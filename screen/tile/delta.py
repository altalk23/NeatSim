import pygame as pg
from math import ceil

class Delta:
    zoom = 0
    dx = 0
    dy = 0
    dz = 1
    pdz = 1
    dirty = 0

    f = lambda self, x: (x+1)**0.7

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.currentWidth = width
        self.currentHeight = height
        self.seenWidth = width
        self.seenHeight = height

    def zoomIn(self):
        if self.zoom < 40:
            self.zoom += 1
            self.setZoom()

    def zoomOut(self):
        if self.zoom > 0:
            self.zoom -= 1
            self.setZoom()

    def setZoom(self):
        self.dz = self.f(self.zoom)



        self.centerX = (self.dx - self.width / 2) / self.pdz #(1 / self.pdz * self.width)/2
        self.centerY = (self.dy - self.height / 2) / self.pdz #(1 / self.pdz * self.height)/2

        self.currentWidth = self.width * self.dz
        self.currentHeight = self.height * self.dz

        self.seenWidth = 1 / self.dz * self.width
        self.seenHeight = 1 / self.dz * self.height


        self.dx += self.centerX * (self.dz - self.pdz)
        self.dy += self.centerY * (self.dz - self.pdz)
        #self.dx = (self.dx) * (self.dz - self.pdz)
        #self.dy = (self.dy) * (self.dz - self.pdz)




        print(self.pdz, self.dz, self.centerX, self.centerY, self.dx, self.dy, "\n")


        self.dx = max(min(self.dx, 0), self.width - self.currentWidth)
        self.dy = max(min(self.dy, 0), self.height - self.currentHeight)

        self.pdz = self.f(self.zoom)
        #print(self.dz, self.dx, self.dy)
        self.dirty = 1

    def move(self, dx, dy):
        self.dx += dx
        self.dy += dy

        self.dirty = 1

        self.dx = max(min(self.dx, 0), self.width - self.currentWidth)
        self.dy = max(min(self.dy, 0), self.height - self.currentHeight)


    def delta(self, rect: pg.Rect) -> pg.Rect:
        rect = rect.copy()
        rect.x = ceil(rect.x * self.dz + self.dx)
        rect.y = ceil(rect.y * self.dz + self.dy)
        rect.w = ceil(rect.w * self.dz)
        rect.h = ceil(rect.h * self.dz)
        return rect
