import pygame
from pygame.locals import *
from random import *
from classes.player import *

class Enemy (pygame.sprite.Sprite):
    def __init__(self,center):
        super(Enemy,self).__init__()
        # Defining attributes for enemy, health, damage dealt to player on succesful attack,
        # movement speed, and damage from any special atrributes the enemy may have(e.g. poison).
        # Also the amount of exp and gold said enemy will drop
        self.surface = pygame.Surface((20,20))
        self.rect = self.surface.get_rect()
        self.surface.fill ("blue")
        self.rect.center = center
        self.health = 5
        self.damage = 1
        self.speed = 2
        self.spec_damage = 1
        self.exp = 1
        self.gold = 1

    def lootdrop(self,gold,exp):
        gold = randint((gold-5),(gold+5))
        exp = randint((exp-50),(exp+50))
        drops = (gold, exp) 
        
        
        
        

        
    def update(self,keys):
        if self.health <= 0:
            self.lootdrop(self.gold, self.exp)
            self.kill()
            #if we decide to do a loot system, make a "drop loot" function and run it here
        






    


