from random import uniform
from math import pi

from screen.sim.sim import Sim

class SimSystem:
    selected = None
    i = 0

    def __init__(self, group, tilesystem):
        self.group = group
        self.tilesystem = tilesystem
        self.delta = tilesystem.delta

    def generateSims(self, count: int) -> None:
        self.sims = []
        for i in range(count):
            x = uniform(0, self.tilesystem.systemWidth)
            y = uniform(0, self.tilesystem.systemHeight)
            r = uniform(0, 360)
            self.sims.append(Sim(self, i))
            self.sims[i].setPosition(x, y)
            self.sims[i].setRotation(r)
            self.sims[i].add(self.group)
        self.group.update()

    def move(self):
        for sim in self.sims:
            if not self.i % 30:
                sim.move(0.1, uniform(0, 360))
            else:
                sim.move(sim.s, sim.r)
        self.i += 1


    '''
    def deltaChange(self):
        for sim in self.sims:
            if self.tilesystem.rect.colliderect(self.delta.delta(sim.baseRect)):
                sim.update()
    '''
    def selectSim(self, pos):
        for sim in self.sims:
            if sim.rect.collidepoint(pos):
                self.selected = sim
                return 1
        self.selected = None
        return 0



    '''
    Updates the position of all sims
    def updateSims(self):
        dz = self.tilesystem.curve(self.tilesystem.dz)
        for sim, position in zip(self.sims.values(), self.positions.values()):
            position.bb.align(dz, self.tilesystem.dx, self.tilesystem.dy)
            sim.updatePosition(position)


    def changeZoom(self):
        dz = self.tilesystem.curve(self.tilesystem.dz)
        for sim, position in zip(self.sims.values(), self.positions.values()):
            position.bb.align(dz, self.tilesystem.dx, self.tilesystem.dy)
            sim.updateScale(position)

    def rot(self):
        for sim, position in zip(self.sims.values(), self.positions.values()):
            position.angle += 0.1
            sim.updateRotation(position)

    def selectSim(self, mousePos):
        for sim, position in zip(self.sims.values(), self.positions.values()):
            if position.bb.collidingPoint(mousePos):
                self.selectedSim = sim
                return 1
        return 0
    '''
