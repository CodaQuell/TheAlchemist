

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
#everything must be in sprite group 1 to get drawn
spriteGroup1 = pygame.sprite.Group()
#enemies
spriteGroup2= pygame.sprite.Group()
#walls
spriteGroup3 = pygame.sprite.Group()
#up and down level points
spriteGroup4 = pygame.sprite.Group()
#everything but player, used for enitiy kill function
spriteGroup5 = pygame.sprite.Group()



#renders the entities for each level
def level1():
  #entry points
  upLevelPoint = newLevel((1900,540),1)

  walltop = Wall((20,20),W*2,40)
  wallbottom = Wall((20,H-20),W*2,40)
  wallleft = Wall((20,20),40,H*2)
  wallright1 = Wall((W-20,20),40,H-80)
  wallright2 = Wall((W-20,H),40,H-40)


  #all playes/entities
  spriteGroup1.add(upLevelPoint)
  spriteGroup1.add(player)



  #walls or solid blocks
  spriteGroup3.add(walltop)
  spriteGroup3.add(wallbottom)
  spriteGroup3.add(wallleft)
  spriteGroup3.add(wallright1)
  spriteGroup3.add(wallright2)


  #entry/exit points
  spriteGroup4.add(upLevelPoint)

  spriteGroup5.add(walltop)
  spriteGroup5.add(wallbottom)
  spriteGroup5.add(wallleft)
  spriteGroup5.add(wallright1)
  spriteGroup5.add(wallright2) 
  spriteGroup5.add(upLevelPoint)
  
def level2():
  

  #entry points
  upLevelPoint = newLevel((1900,540),1)
  downLevelPoint = newLevel((20,540),0)

  walltop = Wall((20,20),W*2,40)
  wallbottom = Wall((20,H-20),W*2,40)
  wallright1 = Wall((W-20,20),40,H-80)
  wallright2 = Wall((W-20,H),40,H-40)
  sheep = Sheep(2,0,(300,600))


  #all playes/entities
  spriteGroup1.add(upLevelPoint)
  spriteGroup1.add(downLevelPoint)
  spriteGroup1.add(player)
  spriteGroup1.add(sheep)

  #all enemies
  spriteGroup2.add(sheep)



  #walls or solid blocks
  spriteGroup3.add(walltop)
  spriteGroup3.add(wallbottom)
  #spriteGroup3.add(wallleft)
  spriteGroup3.add(wallright1)
  spriteGroup3.add(wallright2)


  #entry/exit points
  spriteGroup4.add(upLevelPoint)
  spriteGroup4.add(downLevelPoint)

  spriteGroup5.add(walltop)
  spriteGroup5.add(wallbottom)
  spriteGroup5.add(wallright1)
  spriteGroup5.add(wallright2)
  spriteGroup5.add(sheep)
  spriteGroup5.add(upLevelPoint)
  spriteGroup5.add(downLevelPoint)

def level3():
  

  #entry points
  downLevelPoint = newLevel((20,540),0)

  walltop = Wall((20,20),W*2,40)
  wallbottom = Wall((20,H-20),W*2,40)
  wallright1 = Wall((W-20,20),40,H-80)
  wallright2 = Wall((W-20,H),40,H-40)
  sheep1 = Sheep(2,0,(600,600))
  sheep2 = Sheep(2,0,(700,100))


  #all playes/entities
  spriteGroup1.add(downLevelPoint)
  spriteGroup1.add(player)
  spriteGroup1.add(sheep1)
  spriteGroup1.add(sheep2)

  #all enemies
  spriteGroup2.add(sheep1)
  spriteGroup2.add(sheep2)



  #walls or solid blocks
  spriteGroup3.add(walltop)
  spriteGroup3.add(wallbottom)
  #spriteGroup3.add(wallleft)
  spriteGroup3.add(wallright1)
  spriteGroup3.add(wallright2)


  #entry/exit points
  spriteGroup4.add(downLevelPoint)

  spriteGroup5.add(walltop)
  spriteGroup5.add(wallbottom)
  spriteGroup5.add(wallright1)
  spriteGroup5.add(wallright2)
  spriteGroup5.add(sheep1)
  spriteGroup5.add(sheep2)
  spriteGroup5.add(downLevelPoint)


#kills all enities thta are in sprite group 5, should be everything but player
def entityKill():
  for enitiy in spriteGroup5:
    enitiy.kill()
    
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
