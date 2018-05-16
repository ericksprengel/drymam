#!/usr/bin/env monkeyrunner
import sys, copy
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import eyes
import sys, os
import random

DRAG_DELAY = 0.1
DRAG_STEPS = 15
DRAG_DISTANCE = 100




class areas:
  ACCELERATOR = ((2300,1100),(2330,1300))
  BRAKE =       (( 160,1100),( 220,1300))

  PAUSE =       ((2410,  90),(2420, 120))

  OUT_OF_FUEL = ((1230,1100),(1240,1300))
#  OUT_OF_FUEL =  (( 550,1100),( 560,1300))
  TRY_AGAIN =   (( 580,1100),( 590,1300))
  

def get_gameplay():
  f = open("gameplay.txt", "r")
  gameplay = []
  for line in f.readlines():
    cmd = line.strip().split(":")
    action = cmd[0]
    duration = int(cmd[1])/1000.0
    sleep = int(cmd[2])/1000.0 if len(cmd) > 2 else 0.4
    gameplay.append( ( action, duration, sleep ))
  return gameplay

def should_pause():
  f = open("config.txt", "r")
  for line in f.readlines():
    entry = line.strip().split("=")
    if entry[0] == "status":
      return entry[1] in [ "pause", "p" ]
  return False

def should_stop():
  f = open("config.txt", "r")
  for line in f.readlines():
    entry = line.strip().split("=")
    if entry[0] == "status":
      return entry[1] in [ "stop", "s" ]
  return False

def tap_on_area(device, area, sleep, debug=False):
  tap = (
      random.randint(area[0][0], area[1][0]),
      random.randint(area[0][1], area[1][1])
    )
  if debug:
    print("click: %s" % (tap,) )
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(sleep)


def hold_on_area(device, area, duration, sleep, debug=False):
  tap = (
      random.randint(area[0][0], area[1][0]),
      random.randint(area[0][1], area[1][1])
    )
  if debug:
    print("click: %s" % (tap,) )
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN)
  MonkeyRunner.sleep(duration)
  device.touch(tap[0],tap[1],MonkeyDevice.UP)
  MonkeyRunner.sleep(sleep)


def accelerate(device, duration, sleep=0.4):
  print("accelerate: %f" % (duration))
  hold_on_area(device, areas.ACCELERATOR, duration, sleep)

def brake(device, duration, sleep=0.4):
  print("brake: %f" % (duration))
  hold_on_area(device, areas.BRAKE, duration, sleep)

def restart_game(device):
  print("restart_game") 
#  tap_on_area(device, areas.PAUSE, 0.5)
  tap_on_area(device, areas.OUT_OF_FUEL, 0.2)
  tap_on_area(device, areas.TRY_AGAIN, 0.2)
  #MonkeyRunner.sleep(5.0)

def iterate(device):
#  for i in range(4):
#    accelerate(device, random.random()*0.3 + 0.1)
  for idx, (action, duration, sleep) in enumerate(get_gameplay()):
    print("action: %d" % idx)
    if action == "A":
      accelerate(device, duration, sleep)
    elif action == "B":
      brake(device, duration, sleep)
    elif action == "S":
      MonkeyRunner.sleep(duration)

  restart_game(device)
  
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

#while True:
for j in range(7000):
  print("ITERATION: %d" % (j) )
  iterate(device)
  if should_stop():
    sys.exit(0)
  
  while should_pause():
    MonkeyRunner.sleep(1.0)



# Takes a screenshot
#result = device.takeSnapshot()

# Output file image
#fileImage = os.path.join(os.path.dirname(os.sys.argv[0]), "shot1.png")

# Writes the screenshot to a file
#result.writeToFile(fileImage,'png')

