import pygame

class Enemy (pygame.sprite.Sprite):
    def __intit__(self,health,damage,speed,spec_damage):
        
        # Defining attributes for enemy, health, damage dealt to player on succesful attack,
        # movement speed, and damage from any special atrributes the enemy may have(e.g. poison).
        self.health = health
        self.damage = damage
        self.speed = speed
        self.spec_damage = spec_damage
    def update(self):
        if self.health >= 0:
            self.kill
            #if we decide to do a loot system, make a "drop loot" function and run it here