import pygame
from pygame.locals import *

import random
from random import *

#creates wall class with a health, a surface, and a spawn draw point
class Sheep(pygame.sprite.Sprite):
    def __init__(self,health,speed,center):
        super(Sheep,self).__init__()
        self.health = health
        self.speed = speed
        self.surface = pygame.Surface((40,20))
        self.rect = self.surface.get_rect()
        self.surface.fill ("green")
        self.rect.center = center
