"""
ideas for future:
  tile map:
    an idea to make puting items in place would be to make a grind on the screen, like we have now with H and W, but using the values 160 and 90 (or 1600 by 900)
    we would use 160:90 because all the monitors that we work on should in theory have a 16:9 aspect ratio, where as the resolution for some of them is different. 
    using with we would make all our maps with those dimetions, and it would help alot with knowing where to place items like walls. 
  image shifter:
    every time we go up or down a level we just render a new image from the assets folder, set the playes stats in a file or variable.
    we would then kill all the entities and redraw the new ones. 
    an issue with this is that if the player chose to go back down a level of the tower (if thats and option), the entities from that level would be redrawn.
    this could lead to easy loot drops, entity farming, braking game progress.
  attacks func for player:
    not sure how to go about making this one yet, will continue to expand on ideas...

"""

#3rd party libaries import
import sys
import tkinter
import pygame
from pygame.locals import *
import random
from random import *

#import classs, funcs, and assets to the index
from classes.playerClass import Player
from classes.enemyClass import Enemy 
from classes.enemyClass import *
from classes.sheepClass import * 
from classes.wallClass import Wall
from classes.newLevelClass import newLevel


from functions.backgound import background
from functions.backgound import current_image
from functions.backgound import next_image
from functions.backgound import prev_image
from functions.backgound import image_list

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

#init player from Player class
player = Player(H,W)

#create sprite group
spriteGroup1 = pygame.sprite.Group()
spriteGroup2= pygame.sprite.Group()
spriteGroup3 = pygame.sprite.Group()
spriteGroup4 = pygame.sprite.Group()


def level1():
  #entry points
  upLevelPoint = newLevel((1900,540),1)

  wall0 = Wall((W-50,H-50))
  wall1 = Wall((W-50,H-70))
  wall2 = Wall((W-50,H-90))

  #all playes/entities
  spriteGroup1.add(upLevelPoint)
  spriteGroup1.add(player)
  spriteGroup1.add(wall0)

  #walls or solid blocks
  spriteGroup3.add(wall0)


  #entry/exit points
  spriteGroup4.add(upLevelPoint)





#stores players location on x,y plane, used to set position apon collision 
tempPlayerPos = player.rect.center

# Game loop
while True:
  #gets selected background image from background func
  background(current_image,W,H,screen)
  level1()
  
  #checks for esc key pressed to exit game
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

  for lvl in spriteGroup4:
    if pygame.sprite.collide_rect(player,lvl):
      if lvl.num == 1:
        player.rect.center = (300,300)
        next_image(current_image,W,H,screen)
        
      elif lvl.num == 0:
        if image_list[0] == "C:\\Users\\josso\\Downloads\\tower-game-main\\tower-game-main\\main\\assets\\background0.png":
          pass
        else:
          prev_image(current_image,W,H,screen)
       
  #updates the screen ever 60 ticks. This is set in fpsClock
  pygame.display.update()
  fpsClock.tick(fps)
