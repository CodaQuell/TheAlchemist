import pygame
import random

class Enemy (pygame.sprite.Sprite):
    def __intit__(self,health,damage,speed,spec_damage,exp,gold):
        
        # Defining attributes for enemy, health, damage dealt to player on succesful attack,
        # movement speed, and damage from any special atrributes the enemy may have(e.g. poison).
        # Also the amount of exp and gold said enemy will drop
        self.health = health
        self.damage = damage
        self.speed = speed
        self.spec_damage = spec_damage
        self.exp = exp
        self.gold = gold

    def lootdrop(gold,exp):
        gold = random.randint((gold-5),(gold+5))
        exp = random.randint((exp-50),(exp+50))
        drops = (gold, exp) 
        print (drops)
        
        

        
    def update(self):
        if self.health >= 0:
            self.kill
            #if we decide to do a loot system, make a "drop loot" function and run it here





