import pygame
from character import *
from colours import *
from platforms import *

"""
pygame.transform.flip will flip an image in theory
"""
pygame.init()

display_width = 800
display_height = 600
FPS = 60


clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Platformer")

gameExit = False
ground_height = 25

mario = MainChar("Mario")

while not gameExit:
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, green, (0,750, display_width, display_height))
    drawPlatforms()
    mario.detectCollision()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mario.move("left")
            elif event.key == pygame.K_RIGHT:
                mario.move("right")
            elif event.key == pygame.K_UP:
                mario.startJump()
            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_p:
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mario.move("stop")
            elif event.key == pygame.K_UP:
                mario.endJump()
            elif event.key == pygame.K_DOWN:
                pass

    pygame.draw.rect(gameDisplay, grey, [0,display_height-ground_height,display_width,display_height])

    mario.updatePos()
    mario.draw()

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
quit()