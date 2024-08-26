import pygame
from pygame.locals import *
from random import *

class Enemy (pygame.sprite.Sprite):
    def __init__(self,health,damage,speed,spec_damage,exp,gold):
        super(Enemy,self).__init__()
        # Defining attributes for enemy, health, damage dealt to player on succesful attack,
        # movement speed, and damage from any special atrributes the enemy may have(e.g. poison).
        # Also the amount of exp and gold said enemy will drop
        self.surface = pygame.Surface((20,20))
        self.rect = self.surface.get_rect()
        self.surface.fill ("blue")
        self.rect.center = [600,300]
        self.health = health
        self.damage = damage
        self.speed = speed
        self.spec_damage = spec_damage
        self.exp = exp
        self.gold = gold

    def lootdrop(self,keys,gold,exp,frames):
        gold = randint((gold-5),(gold+5))
        exp = randint((exp-50),(exp+50))
        drops = (gold, exp) 
        if frames == 1:

            print (drops)
        
        
        

        
    def update(self,keys,lootdrop,gold,exp):
        if self.health >= 0:
            self.kill
            lootdrop(self,gold,exp,-1)
            #if we decide to do a loot system, make a "drop loot" function and run it here




    


