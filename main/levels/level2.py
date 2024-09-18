import pygame
from pygame.locals import *
import random
import tkinter
from classes.player import player

from classes.playerClass import *
from classes.enemyClass import *
from classes.enemyClass import *
from classes.sheepClass import * 
from classes.wallClass import *
from classes.newLevelClass import *

from functions.spriteGroups import *

app = tkinter.Tk()
W = app.winfo_screenwidth()
H = app.winfo_screenheight()

def level2():
  

  #entry points
  upLevelPoint = newLevel((1898, 986),1)
  downLevelPoint = newLevel((11, 84),0)
  spriteGroup1.add(upLevelPoint)
  spriteGroup1.add(downLevelPoint)
  spriteGroup1.add(player)
  spriteGroup4.add(upLevelPoint)
  spriteGroup4.add(downLevelPoint)
  spriteGroup5.add(upLevelPoint)
  spriteGroup5.add(downLevelPoint)

  wall0 = Wall((30, 142),56,56)
  spriteGroup1.add(wall0)
  spriteGroup3.add(wall0)
  spriteGroup5.add(wall0)
  wall1 = Wall((26, 191),56,56)
  spriteGroup1.add(wall1)
  spriteGroup3.add(wall1)
  spriteGroup5.add(wall1)
  wall2 = Wall((21, 231),56,56)
  spriteGroup1.add(wall2)
  spriteGroup3.add(wall2)
  spriteGroup5.add(wall2)
  wall3 = Wall((16, 270),56,56)
  spriteGroup1.add(wall3)
  spriteGroup3.add(wall3)
  spriteGroup5.add(wall3)
  wall4 = Wall((17, 306),56,56)
  spriteGroup1.add(wall4)
  spriteGroup3.add(wall4)
  spriteGroup5.add(wall4)
  wall5 = Wall((17, 349),56,56)
  spriteGroup1.add(wall5)
  spriteGroup3.add(wall5)
  spriteGroup5.add(wall5)
