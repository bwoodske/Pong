import pygame
from constants import *


class Player:
    def __init__(self, name, pnum):
        self.name = name
        self.pnum = pnum
        self.ypos = 100
        self.width = 20
        self.height = 80
        self.momentum = 0
        self.keydown = [0, 0]
        self.move_speed = 7

        if pnum == 1:
            self.xpos = 50
        elif pnum == 2:
            self.xpos = 930

    def moveUp(self):
        self.momentum = -self.move_speed
        self.keydown[0] = 1

    def moveDown(self):
        self.momentum = +self.move_speed
        self.keydown[1] = 1

    def stop(self, direction):
        if direction == "up":
            self.keydown[0] = 0
        elif direction == "down":
            self.keydown[1] = 0

        if self.keydown == [0, 0]:
            self.momentum = 0

    def draw(self):
        self.ypos += self.momentum

        if self.ypos < 0:
            self.ypos = 0
            self.momentum = 0

        if self.ypos + self.height > display_height:
            self.ypos = (display_height - self.height)
            self.momentum = 0

        pygame.draw.rect(gameDisplay, white, [self.xpos, self.ypos, self.width, self.height])