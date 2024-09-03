#3rd party libaries import
import sys
import tkinter

import pygame
from pygame.locals import *


import random
from random import *

from classes.playerClass import Player
from classes.enemyClass import Enemy 
from classes.enemyClass import *
from classes.sheepClass import * 
from classes.wallClass import Wall


# getting height and width for the game window
# an included module, hopefully school computers have it.
app = tkinter.Tk()
W = app.winfo_screenwidth()
H = app.winfo_screenheight()



#init pygame
pygame.init()

#geting tick rate for the game time
fps = 60
fpsClock = pygame.time.Clock()






screen = pygame.display.set_mode((W,H))




#init player from Player class
player = Player(H,W)
enemy = Enemy(20,2,3,0,60,34)
sheep = Sheep(5,2)
wall = Wall((randint(20,H),randint(20,W)))


#create sprite group
spriteGroup1 = pygame.sprite.Group()
spriteGroup2= pygame.sprite.Group()
spriteGroup3 = pygame.sprite.Group()

#add player+others to respective sprite groups to sprite group
spriteGroup1.add(player)
spriteGroup1.add(wall)
spriteGroup1.add(enemy)
spriteGroup1.add(sheep)
spriteGroup2.add(enemy)
spriteGroup2.add(sheep)
spriteGroup3.add(wall)

# a neccessary variable for collision checking
tempPlayerPos = player.rect.center


# Game loop
while True:
  screen.fill((0, 0, 0))
  
  
  for event in pygame.event.get():

    #makes it so you can either press esc or the x button to quit
    if event.type == QUIT or event.type == KEYDOWN:
      #press esc to exit pygame
      if event.key == K_ESCAPE:

        pygame.quit()
        sys.exit()
    
       
# updating the game when keystrokes are initiated
  keys = pygame.key.get_pressed()
  for sprite in spriteGroup1:
    sprite.update(keys)
   
   # checking for a wall collide, then stopping the player if there is
  wallTouch = False    
  for wall in spriteGroup3:
    if pygame.sprite.collide_rect(player,wall):
      wallTouch = True
  if wallTouch:
    player.rect.center = tempPlayerPos
  else:
    tempPlayerPos = player.rect.center

  for sprite in spriteGroup1:
      screen.blit(sprite.surface,sprite.rect)

      # sets up for colliding with any enemy
      #runs the loot function from enemy class
  for en in spriteGroup2:
    if pygame.sprite.collide_rect(player,en):
       en.health -= 1
       


  #updates the screen ever 60 ticks. This is set in fpsClock
  pygame.display.update()
  fpsClock.tick(fps)
