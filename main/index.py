
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
from levels.level4 import level4
from levels.level5 import level5

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
#n = 0
# Game loop
level_transitioning = False
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
     #Colliders are placed along the player's edges
      playercollider_left = Collider(tempDur, player.rect.left - 20, player.rect.centery - 5, 20, 10)
      playercollider_right = Collider(tempDur, player.rect.right, player.rect.centery - 5, 20, 10)
      playercollider_up = Collider(tempDur, player.rect.centerx - 5, player.rect.top - 20, 10, 20)
      playercollider_down = Collider(tempDur, player.rect.centerx - 5, player.rect.bottom, 10, 20)

      tempMouse = pygame.mouse.get_pos()
      dx = tempMouse[0] - tempPlayerPos[0]
      dy = tempMouse[1] - tempPlayerPos[1]

       #Calculate the angle in radians, and convert to degrees
      angle_radians = math.atan2(dy, dx)
      angle_degrees = math.degrees(angle_radians)

       #Spawn the collider based on the angle direction
      if -45 < angle_degrees < 45:
          spriteGroup1.add(playercollider_right)
      elif 45 <= angle_degrees <= 135:
          spriteGroup1.add(playercollider_down)
      elif angle_degrees < -45 and angle_degrees > -135:
          spriteGroup1.add(playercollider_up)
      else:
          spriteGroup1.add(playercollider_left)
    


    #this is the code i used to make all the maze and put enemies in it, it is far from perfect, but it is what it is
    #if event.type == MOUSEBUTTONDOWN:
      #if event.button == 1:
        #tempWallPlace = pygame.mouse.get_pos()
    
        #print(f"wall{n} = Wall({tempWallPlace},56,56)")
        #print(f"spriteGroup1.add(wall{n})")
        #print(f"spriteGroup3.add(wall{n})")
        #print(f"spriteGroup5.add(wall{n})")
        #n+=1
        #wall= Wall((tempWallPlace),56,56)
        #spriteGroup1.add(wall)


      #elif event.button == 3:
        #tempWallPlace = pygame.mouse.get_pos()
        
        #print(f"enemy{n} = Enemy({tempWallPlace})")
        #print(f"spriteGroup1.add(enemy{n})")
        #print(f"spriteGroup2.add(enemy{n})")
        #print(f"spriteGroup5.add(enemy{n})")
        #n+=1
        #enemy= Enemy((tempWallPlace))
        #spriteGroup1.add(enemy)

    
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
  # getting player and enemy position in each tick
  # getting player and enemy position in each tick
  for en in spriteGroup2:  # Assuming spriteGroup2 is your enemy group
      # Store the enemy's current position before moving
      original_pos = en.rect.center
      
      # Calculate the direction vector from the enemy to the player
      player_pos = pygame.Vector2(player.rect.center)
      enemy_pos = pygame.Vector2(en.rect.center)
      
      direction = player_pos - enemy_pos
      
      # Normalize the direction vector (if not zero) and scale it by the enemy speed
      if direction.length() > 0:
          direction = direction.normalize() * en.speed  # Assuming en has a 'speed' attribute
      
      # Move the enemy to the new position (before checking collision)
      en.rect.center += direction
      
      # Check if the new position would collide with any walls
      collided_with_wall = False
      for wall in spriteGroup3:  # Assuming spriteGroup3 is your wall group
          if en.rect.colliderect(wall.rect):
              collided_with_wall = True
              break  # Exit the loop if a collision is detected
      
      # If a collision with a wall occurred, reset the enemy position
      if collided_with_wall:
          en.rect.center = original_pos  # Reset position to original before movement
      
      # Check for collision between player and enemy
      if pygame.sprite.collide_rect(player, en):
          en.health -= 1
          player.health -= en.damage

          if player.health <= 0:
              print("Game Over!")
              pygame.quit()
              sys.exit()

        
         
  #adds collision with newLevel objects, calls entityKill func, loads new level entities
  for lvl in spriteGroup4:
      # Check collision with player and make sure no other level transition is happening
      if pygame.sprite.collide_rect(player, lvl) and not level_transitioning:
          # Activate the transition flag to prevent multiple transitions
          level_transitioning = True  
          
          if lvl.num == 1:  # Moving to the next level
              level += 1
              entityKill()  # Clear current level entities
              player.rect.center = (79, 88)  # Reset player position
              next_image(current_image, W, H, screen)  # Load next background image

              # Load the correct level based on the updated level variable
              if level == 1:
                  level1()
              elif level == 2:
                  level2()
              elif level == 3:
                  level3()
              elif level == 4:
                  level4()
              elif level == 5:
                  level5()

          elif lvl.num == 0:  # Moving to the previous level
              level -= 1
              entityKill()  # Clear current level entities
              player.rect.center = (79, 88)  # Reset player position
              prev_image(current_image, W, H, screen)  # Load previous background image

              # Load the correct level based on the updated level variable
              if level == 1:
                  level1()
              elif level == 2:
                  level2()
              elif level == 3:
                  level3()
              elif level == 4:
                  level4()
              elif level == 5:
                  level5()

          # Reset the transition flag after the level is loaded and entities are set up
          level_transitioning = False


      
       
  #updates the screen ever 60 ticks. This is set in fpsClock
  pygame.display.update()
  fpsClock.tick(fps)
