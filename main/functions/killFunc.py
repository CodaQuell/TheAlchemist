from functions.spriteGroups import *

#kills all enities thta are in sprite group 5, should be everything but player
def entityKill():
  for enitiy in spriteGroup5:
    enitiy.kill()