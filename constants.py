import pygame

# Vital game config
display_width = 1000
display_height = 600
FPS = 60

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))

max_bounce_angle = 75

# Colours
white = (255,255,255)
black = (0,0,0)

grey = (200,200,200)

red = (200,0,0)
light_red = (255,0,0)

blue = (0,0,255)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (0,155,0)
light_green = (0,255,0)