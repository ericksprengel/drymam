#!/usr/bin/env monkeyrunner
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from time import sleep
import os, sys

def is_empty_block(block):
  px = block.getRawPixel(0,0)
  px_min = [px[0], px[1], px[2], px[3]]
  px_max = [px[0], px[1], px[2], px[3]]

  pxf_min = [-1, 31, 54, 12]
  pxf_max = [-1, 63, 88, 44]

  for x in range(10):
    for y in range(10):
      px = block.getRawPixel(x,y)
      for c in range(0,4):
        if px[c] < px_min[c]:
          px_min[c] = px[c]
        else:
          px_max[c] = px[c]

      #print(px)

  print("min")
  print(px_min)
  print("max")
  print(px_max)
  return {"min": px_min, "max": px_max}


# ALL VARS, PARAMS and OPTIONS INITIALIZATION
IMG_PATH = None

# ALL VARS, PARAMS and OPTIONS TREATMENTS
if len(sys.argv) == 1:
  IMG_PATH = sys.argv[1]
else:
  print("usage: getting_min_max [ PATH ]")

# SCRIPT STARTS HERE

try:

  if IMG_PATH:
    image = MonkeyRunner.loadImageFromFile(IMG_PATH)
  else:
    # Connects to the current device, returning a MonkeyDevice object
    device = MonkeyRunner.waitForConnection()

    # Takes a screenshot
    image = device.takeSnapshot()

  px_min = [-1, 255, 255, 255]
  px_max = [-1, 0, 0, 0]

  # getting a sub image from snapshot?
  for i in range(8):
    for j in range(7):
      x = j*102 + 0    + 102/4
      y = i*112 + 173  + 112/4
      width  = 102/2
      height = 112/2
      #block = result.getSubImage((x,y,width,height))

      if False:
        block.writeToFile('imgs/empties/block_%d_%d.png' % (i,j), 'png')
      else:
        fpath = "imgs/empties/block_%d_%d.png" % (i,j)
        block_empty = MonkeyRunner.loadImageFromFile(fpath)
        print(fpath)
        res = is_empty_block(block_empty)
        for c in range(0,4):
          if res["min"][c] < px_min[c]:
            px_min[c] = res["min"][c]
          else:
            px_max[c] = res["max"][c]
        #block.writeToFile('res/block_%d_%d_T.png' % (i,j), 'png')
  
  print("_____")
  print("min")
  print(px_min)
  print("max")
  print(px_max)
  # Writes the screenshot to a file
  #result.writeToFile('res/full.png','png')
  
except KeyboardInterrupt:
  # USE KEYBOARD INTERRUPT TO TREAT ^C
  sys.exit("{0}Interrupted by user...{1}".format(bcolors.WARNING, bcolors.ENDC))

