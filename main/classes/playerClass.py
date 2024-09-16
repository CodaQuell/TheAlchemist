#imports 3rd part libs
import pygame
from pygame.locals import *
import random
from random import *

#inits playerclass
class Player(pygame.sprite.Sprite):
    def __init__(self,screenH,screenW):
        super(Player,self).__init__()
        #sets basic player stats
        self.surface = pygame.Surface((20,20))
        self.rect = self.surface.get_rect()
        self.surface.fill ("white")
        self.rect.center = [300,300]
        self.speed = 10
        self.screenH = screenH
        self.screenW = screenW

    #checks if keys are pressed, then moves accoss x,y plane in accouding direction
    def update(self, keys_pressed):
        if keys_pressed[K_w] or keys_pressed[K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[K_s] or keys_pressed[K_DOWN]:
            self.rect.y += self.speed
        if keys_pressed[K_a] or keys_pressed[K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[K_d] or keys_pressed[K_RIGHT]:
            self.rect.x += self.speed

        #prevents the player from leaving the confines of the screen
        if self.rect.bottom > self.screenH:
            self.rect.bottom = self.screenH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screenW:
            self.rect.right = self.screenW        

            

