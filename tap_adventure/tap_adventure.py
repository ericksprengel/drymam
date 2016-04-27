#!/usr/bin/env monkeyrunner
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys, os
import random

class areas:
  GAME_VIEW = (( 80,  275),(625,  380))
  SKILL_01  = ((515,  625),(640,  675))
  SKILL_02  = ((515,  735),(640,  795))
  SKILL_03  = ((515,  830),(640,  915))
  SKILL_04  = ((515,  955),(640, 1035))
  SKILL_05  = ((515, 1070),(640, 1155))
  
  MENU_HEROES_OPEN  = (( 66, 975),(135, 1000))
  MENU_HEROES_CLOSE = (( 66, 125),(135,  150))

  # first heroe x: 54.
  # distance between heroes: 86
  # x range: -10,+10
  HEROES = [ (( 54 + 86*i - 10, 1045),( 54 + 86*i + 10, 1155)) for i in range(0,8) ]



def tap_on_area(device, area, sleep, debug=False):
  tap = (
      random.randint(area[0][0], area[1][0]),
      random.randint(area[0][1], area[1][1])
    )
  if debug:
    print("click: %s" % (tap,) )
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(sleep)

def upgrade_heroe_skill(heroe_idx):
  # list HEROES
  tap_on_area(device, areas.MENU_HEROES_OPEN, 1.0)

  # open HEROE 00 (it's me!)
  tap_on_area(device, areas.HEROES[heroe_idx], 1.0)

  #click 3 skill_01
  for i in range(5):
    tap_on_area(device, areas.SKILL_02, 0.3)
    tap_on_area(device, areas.SKILL_01, 0.3)

  # close HEROE
  tap_on_area(device, areas.MENU_HEROES_CLOSE, 1.0)


def iterate(device):
  # Hit them!
  for i in range(10):
    print("Hit! %d/10" % (i+1) )
    for j in range(500):
      tap_on_area(device, areas.GAME_VIEW, 0.1)

  upgrade_heroe_skill(random.choice([0,0,0,1,2,3,4,5]))
  

  
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

#while True:
for j in range(10):
  print("ITERATION: %d" % (j) )
  iterate(device)



# Takes a screenshot
#result = device.takeSnapshot()

# Output file image
#fileImage = os.path.join(os.path.dirname(os.sys.argv[0]), "shot1.png")

# Writes the screenshot to a file
#result.writeToFile(fileImage,'png')
