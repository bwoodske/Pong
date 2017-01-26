import pygame
import math
from constants import *
from player import *


class Ball:
    def __init__(self):
        self.xpos = 200
        self.ypos = 100
        self.size = 20
        self.speed = 10
        self.xspeed = 5
        self.yspeed = 5

    def draw(self, p1_ypos, p2_ypos, p_width, p_height):
        self.xpos += self.xspeed
        self.ypos += self.yspeed

        # Floor and ceiling ball bounces
        if (self.ypos < 0) or (self.ypos + self.size > display_height):
            if self.ypos + self.size > display_height:
                self.ypos -= self.yspeed*2
            else:
                self.ypos *= -1
            self.yspeed *= -1

        # Side wall detection
        if (self.xpos < 0) or (self.xpos + self.size > display_width):
            self.xpos -= self.xspeed*2
            self.xspeed *= -1

        # Left paddle collision
        if self.xpos > 50 and self.xpos < 50 + p_width and self.ypos + self.size - 1 > p1_ypos and self.ypos < p1_ypos + p_height:
            relativeIntersectY = (p1_ypos+(p_height/2)) - (self.ypos+((self.size-1)/2))
            normalizedRelativeIntersectionY = (relativeIntersectY/(p_height/2))
            bounceAngle = normalizedRelativeIntersectionY * max_bounce_angle

            self.xspeed = self.speed * math.cos(bounceAngle)
            self.yspeed = self.speed * math.sin(bounceAngle)

            print(self.xspeed, " ", self.yspeed)


        # Right paddle collision
        if self.xpos + self.size - 1 > 930 and self.xpos + self.size - 1 < 930 + p_width and self.ypos + self.size - 1 > p2_ypos and self.ypos < p2_ypos + p_height:
            self.xpos -= self.xspeed*2
            self.xspeed *= -1


        pygame.draw.rect(gameDisplay, white, [self.xpos, self.ypos, self.size, self.size])

    def explosion(self, x, y, size):
        pass