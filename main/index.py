#3rd party libaries import
import sys
import pygame
import random

from pygame.locals import *
from random import *

#initialising pygame
pygame.init()

#geting tick rate for the game time
fps = 60
fpsClock = pygame.time.Clock()
 
#getting height and width for the game window, should fullscreen on *most monitors
W = 1920
H = 1080
screen = pygame.display.set_mode((W,H))
 
# Game loop.
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():

    #makes it so you can iether press esc or the x button to quit
    if event.type == QUIT or event.type == KEYDOWN:
      #press esc to exit pygame
      if event.key == K_ESCAPE:

        pygame.quit()
        sys.exit()
  

  #updates the screen ever 60 ticks. This is set in fpsClock
  pygame.display.update()
  fpsClock.tick(fps)