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
#import tkinter
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
from functions.backgound import background
from functions.backgound import current_image
from functions.backgound import next_image

# getting height and width for the game window
# an included module, hopefully school computers have it.
#app = tkinter.Tk()
#W = app.winfo_screenwidth()
#H = app.winfo_screenheight()
W = 2560
H = 1440


#init pygame
pygame.init()

#geting tick rate for the game time
fps = 30
fpsClock = pygame.time.Clock()

#inits the sceen with the the H and W defined earlier
screen = pygame.display.set_mode((W,H))

#init player from Player class
player = Player(H,W)

#inits other sprites using
enemy = Enemy(20,2,3,0,60,34)
sheep = Sheep(5,2)
wall = Wall((randint(20,H),randint(20,W)))

#create sprite group
spriteGroup1 = pygame.sprite.Group()
spriteGroup2= pygame.sprite.Group()
spriteGroup3 = pygame.sprite.Group()

#add player+others to respective sprite groups to sprite group
#must be in sprite group1 to be drawn onto screen
spriteGroup1.add(player)
spriteGroup1.add(wall)
spriteGroup1.add(enemy)
spriteGroup1.add(sheep)

#non playerable entites, animals or monsters
spriteGroup2.add(enemy)
spriteGroup2.add(sheep)

#sprite group 3 will be for walls or solid objects
spriteGroup3.add(wall)

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
    

    player.attack(0)
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

       
  #updates the screen ever 60 ticks. This is set in fpsClock
  pygame.display.update()
  fpsClock.tick(fps)
