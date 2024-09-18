import pygame
from pygame.locals import *

import random
from random import *

#creates point for new level
class newLevel(pygame.sprite.Sprite):
    def __init__(self,center,num):
        super(newLevel,self).__init__()
        self.surface = pygame.Surface((20,20))
        self.rect = self.surface.get_rect()
        self.surface.fill ("green")
        self.rect.center = center
        self.num = num
        