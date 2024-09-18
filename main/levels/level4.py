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

def level4():
  

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