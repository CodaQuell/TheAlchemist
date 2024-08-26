#3rd party libaries import
import sys

import pygame
from pygame.locals import *

import random
from random import *

from classes.playerClass import Player
from classes.enemyClass import Enemy 
from classes.enemyClass import *
from classes.wallClass import Wall

from win32api import GetSystemMetrics


#init pygame
pygame.init()

#geting tick rate for the game time
fps = 60
fpsClock = pygame.time.Clock()
frames = 0
#getting height and width for the game window
W = GetSystemMetrics(0)
H = GetSystemMetrics(1)
screen = pygame.display.set_mode((W,H))

#init player from Player class
player = Player()
enemy = Enemy(20,2,3,0,60,34)
wall = Wall((randint(20,GetSystemMetrics(0)),randint(20,GetSystemMetrics(1))))

#create sprite group
spriteGroup1 = pygame.sprite.Group()
spriteGroup2= pygame.sprite.Group()
#add player to sprite group
spriteGroup1.add(player)
spriteGroup1.add(wall)
spriteGroup1.add(enemy)
spriteGroup2.add(enemy)
 
# Game loop
while True:
  screen.fill((0, 0, 0))
  enemy1 = Enemy(1,1,1,0,5,1)
  
  for event in pygame.event.get():

    #makes it so you can either press esc or the x button to quit
    if event.type == QUIT or event.type == KEYDOWN:
      #press esc to exit pygame
      if event.key == K_ESCAPE:

        pygame.quit()
        sys.exit()
    
       

  keys = pygame.key.get_pressed()
  for sprite in spriteGroup1:
    for enemy in spriteGroup2:

      sprite.update(keys, enemy.lootdrop, enemy.gold, enemy.exp)

  for sprite in spriteGroup1:
      screen.blit(sprite.surface,sprite.rect)
      # sets up for colliding with any enemy
      #runs the loot function from enemy class
  for en in spriteGroup2:
    if pygame.sprite.collide_rect(player,en):
       en.lootdrop(6,60,1, frames)
  frames +=1
  #updates the screen ever 60 ticks. This is set in fpsClock
  pygame.display.update()
  fpsClock.tick(fps)

