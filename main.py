import pygame
from constants import *
from player import *
from ball import *

pygame.init()

pygame.display.set_caption("Pong")

gameExit = False

left_player = Player("Brett", 1)
right_player = Player("Challenger", 2)
ball = Ball()

while not gameExit:
    gameDisplay.fill(black)

    pygame.draw.rect(gameDisplay, white, [(display_width/2)-1, 0, 2, display_height])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                gameExit = True

        # Player 1 inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_player.moveUp()
            elif event.key == pygame.K_s:
                left_player.moveDown()
            elif event.key == pygame.K_p:
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                left_player.stop("up")
            elif event.key == pygame.K_s:
                left_player.stop("down")

        # Player 2 inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_player.moveUp()
            elif event.key == pygame.K_DOWN:
                right_player.moveDown()
            elif event.key == pygame.K_p:
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                right_player.stop("up")
            elif event.key == pygame.K_DOWN:
                right_player.stop("down")

    left_player.draw()
    right_player.draw()
    ball.draw(left_player.ypos, right_player.ypos, left_player.width, left_player.height)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
quit()