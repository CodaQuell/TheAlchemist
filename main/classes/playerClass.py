#imports 3rd part libs
import pygame
from pygame.locals import *
import random
from random import *
import time


#inits playerclass
class Player(pygame.sprite.Sprite):
    def __init__(self,screenH,screenW):
        super(Player,self).__init__()
        #sets basic player stats
        self.surface = pygame.Surface((20,20))
        self.rect = self.surface.get_rect()
        self.surface.fill ("white")
        self.rect.center = [300,300]
        self.speed = 7
        self.screenH = screenH
        self.screenW = screenW


      
    def attack(self,charge):
        charge = 10
        state = pygame.mouse.get_pressed()
        if state == 1:
            hitrange = Collider(2,10)
            charge -= 1
            pygame.time.wait(5000)
            hitrange.kill()
        if state == 2:
            hitrange = Collider(4,15)
            charge -= 2
            pygame.time.wait(5000)
            hitrange.kill()

        


            
            
        

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

            
class Collider(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Collider,self).__init__()
        x = x
        y = y
        vert = (x,y)
        #sets basic player stats
        self.surface = pygame.Surface((vert))
        self.rect = self.surface.get_rect()
        self.surface.fill("white")
            

