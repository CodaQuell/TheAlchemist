
"THIS DOES NOT WORK YET"

#3rd party libaries import
import sys
import tkinter
import pygame
from pygame.locals import *
import random
from random import *
import time
import math

#import classs, funcs, and assets to the index
from classes.playerClass import *
from classes.enemyClass import *
from classes.enemyClass import *
from classes.sheepClass import * 
from classes.wallClass import *
from classes.newLevelClass import *
from classes.player import player



from functions.backgound import background
from functions.backgound import current_image
from functions.backgound import next_image
from functions.backgound import prev_image
from functions.killFunc import entityKill

from functions.spriteGroups import *

from levels.level1 import level1
from levels.level2 import level2
from levels.level3 import level3

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

#inits the sceen with the the H and W defined earlier
screen = pygame.display.set_mode((W,H))


#checks what level is loaded
level = 1
level1()
#stores players location on x,y plane, used to set position apon collision 
tempPlayerPos = player.rect.center



# Game loop
while True:
  #gets selected background image from background func
  background(current_image,W,H,screen)

  
  
  #checks for esc key pressed to exit game
  for event in pygame.event.get():

    #makes it so you can either press esc or the x button to quit
    if event.type == QUIT or event.type == KEYDOWN:
      #press esc to exit pygame
      if event.key == K_ESCAPE:

        pygame.quit()
        sys.exit()

        

     
    tempDur = .3    
    if event.type == MOUSEBUTTONDOWN:
      playercollider_left = Collider(tempDur,player.rect.left,player.rect.centery,20,10)
      playercollider_right = Collider(tempDur,player.rect.right,player.rect.centery,40,10)
      playercollider_up = Collider(tempDur,player.rect.centerx,player.rect.top,10,20)
      playercollider_down = Collider(tempDur,player.rect.centerx,player.rect.bottom,10,40)

      tempMouse = pygame.mouse.get_pos()
      degrees_x = tempMouse[0] - tempPlayerPos[0]
      degrees_y = tempMouse[1] - tempPlayerPos[1]

      # Calculate the angle in radians
      angle_radians = math.atan2(degrees_x, degrees_y)

      # convert to degrees
      angle_degrees = math.degrees(angle_radians)

      if -45 < angle_degrees < 45:
        spriteGroup1.add (playercollider_down)

      if 45 < angle_degrees < 135:
        spriteGroup1.add (playercollider_right)

      
      if 135 < angle_degrees and angle_degrees < -135:
        spriteGroup1.add (playercollider_up)

      if -135 < angle_degrees and angle_degrees > -45:
        spriteGroup1.add (playercollider_left)
        
        

      
          
    
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
    #resets player pos to the preveously stored value from outside game loop
    player.rect.center = tempPlayerPos
  else:
    #otherwise sets current pos as the temp pos, does with every game tick
    tempPlayerPos = player.rect.center

  for sprite in spriteGroup1:
      screen.blit(sprite.surface,sprite.rect)

      # sets up for colliding with any enemy
      #runs the loot function from enemy class
  for en in spriteGroup2:
    if pygame.sprite.collide_rect(player,en):
       en.health -= 1
       #next_image(current_image,W,H,screen)

  #adds collition with newLevel objects, calles enitiy kill func, loads new level enities
  for lvl in spriteGroup4:
    if pygame.sprite.collide_rect(player,lvl):
      if lvl.num == 1:
        level += 1
        entityKill()
        player.rect.center = (300,300)
        #loads image from from image loader func today
        next_image(current_image,W,H,screen)
        if level == 1:
          level1()
        elif level == 2:
          level2()
        elif level == 3:
          level3()
        
        
      elif lvl.num == 0:
        level -= 1
        entityKill()
        player.rect.center = (300,300)
        prev_image(current_image,W,H,screen)
        if level == 1:
          level1()
        elif level == 2:
          level2()
        elif level == 3:
          level3()
       
  #updates the screen ever 60 ticks. This is set in fpsClock
  pygame.display.update()
  fpsClock.tick(fps)
