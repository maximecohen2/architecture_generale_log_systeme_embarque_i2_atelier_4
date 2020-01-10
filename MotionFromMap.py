#!/usr/bin/env python3
# coding: utf-8

from IMotion import IMotion

defaultpos = [1, 1]
defaultrot = [1, 0]


class MotionFromMap(IMotion):

    def __init__(self, file, startpos=None, startrot=None):
        self.pos = defaultpos if startpos is None else startpos
        self.rot = defaultrot if startrot is None else startrot
        self.world = []
        with open(file, 'r') as f:
            self.world = f.read().splitlines()

    def check_pos(self, pos):
        if self.world[pos[1]][pos[0]] == '*':
            return False
        else:
            return True

    def move(self, distance):
        nextpos = [self.pos[0] + self.rot[0], self.pos[1] + self.rot[1]]
        if self.check_pos(nextpos):
            self.pos = nextpos
            return True
        return False

    def rotate(self, angle):
        if angle == 1:
            self.rot = [1, 0]
        elif angle == 2:
            self.rot = [0, 1]
        elif angle == 3:
            self.rot = [-1, 0]
        elif angle == 4:
            self.rot = [0, -1]

    def __str__(self):
        return "Le bot est en position {x}, {y}".format(x=self.pos[0], y=self.pos[1])


if __name__ == '__main__':
    c = MotionFromMap("maps/map1")
    c.rotate(2)
    print(c.move(10))
    print(c)