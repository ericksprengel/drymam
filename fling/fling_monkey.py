#!/usr/bin/env monkeyrunner
import sys, copy
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import fling_eyes

DRAG_DELAY = 0.1
DRAG_STEPS = 15
DRAG_DISTANCE = 100

def move_left(device, i,j):
  x = j*102 + 0    + 102/2
  y = i*112 + 173  + 112/2    
  device.drag( (x, y), (x - DRAG_DISTANCE, y), DRAG_DELAY, DRAG_STEPS)

def move_right(device, i,j):
  x = j*102 + 0    + 102/2
  y = i*112 + 173  + 112/2    
  device.drag( (x, y), (x + DRAG_DISTANCE, y), DRAG_DELAY, DRAG_STEPS)

def move_up(device, i,j):
  x = j*102 + 0    + 102/2
  y = i*112 + 173  + 112/2    
  device.drag( (x, y), (x, y - DRAG_DISTANCE), DRAG_DELAY, DRAG_STEPS)

def move_down(device, i,j):
  x = j*102 + 0    + 102/2
  y = i*112 + 173  + 112/2    
  device.drag( (x, y), (x, y + DRAG_DISTANCE), DRAG_DELAY, DRAG_STEPS)

def move(device, m):
  if m[0] == 'L':
    move_left(device, m[1][0],m[1][1])
  elif m[0] == 'R':
    move_right(device, m[1][0],m[1][1])
  elif m[0] == 'U':
    move_up(device, m[1][0],m[1][1])
  elif m[0] == 'D':
    move_down(device, m[1][0],m[1][1])
  else:
    raise Exception("WTF?")


def main():
  # Connects to the current device, returning a MonkeyDevice object
  device = MonkeyRunner.waitForConnection()

  move(device, ('L', (3, 4)))

if __name__ == '__main__':
  main()
