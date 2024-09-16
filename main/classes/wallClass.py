import pygame
from pygame.locals import *

import random
from random import *

#creates wall class with a health, a surface, and a spawn draw point
class Wall(pygame.sprite.Sprite):
    def __init__(self,center,size1, size2):
        super(Wall,self).__init__()
        self.health = 32755
        self.surface = pygame.Surface((size1,size2))
        self.rect = self.surface.get_rect()
        self.surface.fill ("red")
        self.rect.center = center
