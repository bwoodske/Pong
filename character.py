import pygame
from platforms import platLocations

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

"""
TODO:

1. after falling off a platform a jump is possible when it shouldn't be.
"""

class MainChar:
    def __init__(self, name):
        self.name = name
        self.xPos = 100
        self.yPos = 464
        self.spriteWidth = 49
        self.spriteHeight = 111
        self.floor = 464  # defines the ground location player cannot drop further
        self.xVelocity = 0
        self.xMaxSpeed = 10
        self.yVelocity = 0
        self.gravity = 1
        self.lastDir = "r"

        self.p_sprite = pygame.image.load('ninja_frame1.png')
        self.p_sprite1 = pygame.image.load('ninja_frame2.png')
        self.p_sprite2 = pygame.image.load('ninja_frame3.png')
        self.sprite = [self.p_sprite, self.p_sprite1, self.p_sprite2]

    def startJump(self):
        if self.yVelocity == 0:
            self.yVelocity = -24

    def endJump(self):
        if self.yVelocity < -6:
            self.yVelocity = -6

    def move(self, direction):
        if direction == "right":
            self.xVelocity += 5
            self.lastDir = "r"
        elif direction == "left":
            self.xVelocity -= 5
            self.lastDir = "l"
        elif direction == "stop":
            self.xVelocity = 0

    def detectCollision(self):
        for x in range(0, len(platLocations)):
            # Detecting body within x of platform
            if self.xPos >= platLocations[x][0] and self.xPos <= (platLocations[x][0] + platLocations[x][2]) or \
            (self.xPos + self.spriteWidth) >= platLocations[x][0] and \
            (self.xPos + self.spriteWidth) <= (platLocations[x][0] + platLocations[x][2]):
                #Detecting head hitting bottom of platform
                if self.yPos <= (platLocations[x][1] + platLocations[x][3]) and self.yPos >= platLocations[x][1]:
                    self.yPos = (platLocations[x][1] + platLocations[x][3] + 1)
                    self.yVelocity = 0
                #Detecting feet hitting top of platform
                if (self.yPos + self.spriteHeight) <= platLocations[x][1] + platLocations[x][3] and \
                (self.yPos + self.spriteHeight) >= platLocations[x][1]:
                    self.yPos = (platLocations[x][1] - self.spriteHeight - 1)
                    self.yVelocity = 0

            #Detecting y position of body inline with platform
            if self.yPos <= platLocations[x][1] and (self.yPos + self.spriteHeight) >= platLocations[x][1] or \
            self.yPos <= (platLocations[x][1] + platLocations[x][3]) and \
            (self.yPos + self.spriteHeight) >= (platLocations[x][1] + platLocations[x][3]) or \
            self.yPos <= platLocations[x][1] and self.yPos >= (platLocations[x][1] + platLocations[x][3]):
                #Hitting left side of platform
                if (self.xPos + self.spriteWidth) >= platLocations[x][0] and \
                (self.xPos + self.spriteWidth) <= (platLocations[x][0] + platLocations[x][2]):
                    self.xPos = (platLocations[x][0] - self.spriteWidth)
                #Hitting right side of platform
                if self.xPos >= platLocations[x][0] and self.xPos <= (platLocations[x][0] + platLocations [x][2]):
                    self.xPos = (platLocations[x][0] + platLocations [x][2])
            print(self.yPos, platLocations[1][1], (platLocations[1][1] + platLocations[1][3]))




    def draw(self):
        if self.xVelocity > 0 or self.lastDir == "r":
            gameDisplay.blit(self.sprite[0], (self.xPos, self.yPos))
        elif self.xVelocity < 0 or self.lastDir == "l":
            gameDisplay.blit(pygame.transform.flip(self.sprite[0], 1, 0), (self.xPos, self.yPos))

    def updatePos(self):
        # Movement
        self.xPos += self.xVelocity

        #Jumps
        self.yVelocity += self.gravity
        self.yPos += self.yVelocity

        if self.yPos > self.floor:
            self.yPos = self.floor
            self.yVelocity = 0
