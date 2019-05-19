#!/usr/bin/env monkeyrunner
import sys, copy
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import mj_eyes, mj_monkey, mj_device
from time import sleep
from Queue import Queue

VERBOSE=False

def print_d(str):
  if VERBOSE:
    print str,

def println_d(str):
  if VERBOSE:
    print(str)


def training(device):
  pass
  # touch training button if > 0
  # touch train button 410,880 600,960
  # touch skip 500 until OK button

def play_league():
  pass
  # touch league button (bottom right on main screen)

  #look for battle 1


def main():
  device_id = sys.argv[1]
  iterations = int(sys.argv[2])
  # Connects to the current device, returning a MonkeyDevice object
  device = MonkeyRunner.waitForConnection('', device_id)

  # Takes a screenshot
  snapshot = device.takeSnapshot()


  for it in range(iterations):
    mj_monkey.drag(device, mj_device.drag.DEEP_TO_FOOD_SPAWN, "DEEP_TO_FOOD_SPAWN")
    mj_monkey.sleep(1.0)
    
    for i in range(2):
      mj_monkey.drag(device, mj_device.drag.MOVE_TO_LEFT_FOOD_SPAWN, "MOVE_TO_LEFT_FOOD_SPAWN")
      mj_monkey.sleep(1.0)
    fps = mj_eyes.get_food_points(snapshot)
    for p in fps:
      mj_monkey.touch(device, p)

    for i in range(2):
      mj_monkey.drag(device, mj_device.drag.MOVE_TO_RIGHT_FOOD_SPAWN, "MOVE_TO_RIGHT_FOOD_SPAWN")
      mj_monkey.sleep(1.0)
    fps = mj_eyes.get_food_points(snapshot)
    for p in fps:
      mj_monkey.touch(device, p)

    if it + 1 < iterations:
      print("sleeping...")
      mj_monkey.sleep(120.0)
      print("waking up...")
      mj_monkey.sleep(10.0)



#  fling_monkey.move(device, m)
#  sleep(1.5)


if __name__ == "__main__":
    main()