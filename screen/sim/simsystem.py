from random import uniform
from math import pi

from screen.sim.sim import Sim
from utilities.position import Position
from utilities.coordinate import Coordinate
from utilities.boundingbox import BoundingBox
from utilities.size import Size

class SimSystem:

    def __init__(self, tilesystem, group):
        self.tilesystem = tilesystem
        self.group = group

    def generateSims(self, count: int):
        self.sims = {}
        self.positions = {}
        for i in range(count):
            self.sims[i] = Sim(self.tilesystem, self, i)
            self.sims[i].add(self.group)

            windowSize = self.tilesystem.windowSize.get()
            position = Position(
                BoundingBox(
                    Coordinate(
                        uniform(0, windowSize[0]),
                        uniform(0, windowSize[1])
                    ),
                    Size(
                        16,
                        16,
                    )
                ),
                uniform(0, pi)
            )
            self.sims[i].updateScale(position)
            self.group.change_layer(self.sims[i], 1000)
            self.positions[i] = position

    '''
    Updates the position of all sims
    '''
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
