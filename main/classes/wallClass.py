import pygame
from pygame.locals import *

import random
from random import *

#creates wall class with a health, a surface, and a spawn draw point
class Wall(pygame.sprite.Sprite):
    def __init__(self,center):
        super(Wall,self).__init__()
        self.health = 32755
        self.surface = pygame.Surface((40,40))
        self.rect = self.surface.get_rect()
        self.surface.fill ("red")
        self.rect.center = center
        
