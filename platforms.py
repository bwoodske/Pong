import pygame
from colours import *

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))



platLocations = [(300,320,150,30),
                 (600,450,150,30),
                 (100,150,150,30)]

def drawPlatforms():
    for x in range(0,len(platLocations)):
        pygame.draw.rect(gameDisplay, black, platLocations[x])
