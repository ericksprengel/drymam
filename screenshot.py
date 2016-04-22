#!/usr/bin/env monkeyrunner
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from time import sleep
import os, sys

# ALL VARS, PARAMS and OPTIONS INITIALIZATION
IMG_PATH = None
RECT     = None


# PARAMS AND OPTIONS PARSE
# there is no argparse :(

# ALL VARS, PARAMS and OPTIONS TREATMENTS
if len(sys.argv) == 2:
  IMG_PATH = sys.argv[1]
  RECT = None
elif len(sys.argv) == 6:
  IMG_PATH = sys.argv[1]
  RECT = tuple([ int(x) for x in sys.argv[2:] ])
else:
  print("usage: screenshot PATH [ X Y WIDTH HEIGHT ]\n")
  sys.exit(1)

# SCRIPT STARTS HERE

try:
  # Connects to the current device, returning a MonkeyDevice object
  device = MonkeyRunner.waitForConnection()

  
  # Takes a screenshot
  result = device.takeSnapshot()

  # getting a sub image from snapshot?
  if RECT:
    result = result.getSubImage(RECT)

  print(IMG_PATH)

  # Writes the screenshot to a file
  result.writeToFile(IMG_PATH,'png')
  
except KeyboardInterrupt:
  # USE KEYBOARD INTERRUPT TO TREAT ^C
  sys.exit("{0}Interrupted by user...{1}".format(bcolors.WARNING, bcolors.ENDC))


# sets a variable with the package's internal name
#package = 'com.example.testpixel'

# sets a variable with the name of an Activity in the package
#activity = 'com.example.testpixel.MainActivity'

# sets the name of the component to start
#runComponent = package + '/' + activity

#device.touch(274,470,MonkeyDevice.DOWN_AND_UP)
#sleep(0.05)
#device.drag((100,500),(100,750),2.0,50)

#sleep(2.0)


# Runs the component
#device.startActivity(component=runComponent)

# Presses the Menu button
# device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

