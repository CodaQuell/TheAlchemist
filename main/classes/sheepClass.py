from classes.enemyClass import *

class Sheep (Enemy):
    def __init__(self,health,speed):
        super(Sheep,self).__init__(health,damage=0,speed=speed,spec_damage=0,exp=55,gold=6)
        #self.health = health
        #self.speed = speed
        self.surface = pygame.Surface((40,20))
        self.rect = self.surface.get_rect()
        self.surface.fill ("green")
        self.rect.center = [600,600]