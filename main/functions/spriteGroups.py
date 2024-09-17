import pygame

from pygame.locals import *

#create sprite group
#everything must be in sprite group 1 to get drawn
spriteGroup1 = pygame.sprite.Group()
#enemies
spriteGroup2= pygame.sprite.Group()
#walls
spriteGroup3 = pygame.sprite.Group()
#up and down level points
spriteGroup4 = pygame.sprite.Group()
#everything but player, used for enitiy kill function
spriteGroup5 = pygame.sprite.Group()
#collision boxes for player's attack
spriteGroup6 = pygame.sprite.Group()