import pygame
from pygame.locals import *

import random
from random import *

#creates point for new level
class newLevel(pygame.sprite.Sprite):
    def __init__(self,center,num):
        super(newLevel,self).__init__()
        self.surface = pygame.Surface((40,40))
        self.rect = self.surface.get_rect()
        self.surface.fill ("white")
        self.rect.center = center
        self.num = num
        