#!/usr/bin/env monkeyrunner
# -*- coding: utf-8 -*-
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys, os
import random
import datetime

class areas:
# Press "combate rápido"
  FAST_FIGHT        = (( 730, 585),(1070, 680), "FAST_FIGHT")
  START_FIGHT       = (( 430, 250),( 890, 530), "START_FIGHT")
  OK_BUTTON_VICTORY = (( 570, 630),( 690, 690), "OK_BUTTON_VICTORY")
  OK_BUTTON_DEFENSE = (( 590, 630),( 690, 620), "OK_BUTTON_DEFENSE")

  # first heroe x: 54.
  # distance between heroes: 86
  # x range: -10,+10
  HEROES = [ (( 54 + 86*i - 10, 1045),( 54 + 86*i + 10, 1155)) for i in range(0,8) ]


def has_button_to_dimiss(device):
  print("TODO: has_button_to_dimiss")

def save_screenshot(device, file_path):
  # Takes a screenshot
  result = device.takeSnapshot()
  # Output file image
  fileImage = os.path.join(os.path.dirname(os.sys.argv[0]), file_path)
  # Writes the screenshot to a file
  result.writeToFile(fileImage,'png')


def tap_on_area(device, area, sleep, debug=False):
  tap = (
      random.randint(area[0][0], area[1][0]),
      random.randint(area[0][1], area[1][1])
    )
  if debug:
    now = datetime.datetime.now()
    # http://bugs.jython.org/issue2166
    #save_screenshot(device, "%s_%s_%s.png" % (now.strftime("%y-%m-%d_%H-%M"), now.microsecond, area[2]))
    print("click: %s, %s\t\t%s" % (tap[0], tap[1], area[2]) )
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(sleep)


def iterate(device):
  tap_on_area(device, areas.FAST_FIGHT,         3.0 + random.random()*0.4, True)
  tap_on_area(device, areas.START_FIGHT,       15.0 + random.random()*1.0, True)
  tap_on_area(device, areas.OK_BUTTON_VICTORY,  3.0 + random.random()*0.4, True)



# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

#while True:
for j in range(100):
  print("ITERATION: %d" % (j) )
  iterate(device)
