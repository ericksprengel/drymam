# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys, os
import random

class areas:
  GOLD      = ((900,600),(1000, 750))


# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

def get_tap_on_gold():
  return (
      random.randint(areas.GOLD[0][0], areas.GOLD[1][0]),
      random.randint(areas.GOLD[0][1], areas.GOLD[1][1])
    )

def iterate():
  tap = get_tap_on_gold()
  print("  click: %s" % (tap,) )
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(random.randint(9,12)/1.0)
  

def must_exit():
  f = open('must_exit', 'r')
  request = f.read()
  f.close()
  print(request)
  return request.strip() == "1"

counter = 0
#while True:
for j in range(1000):
  if must_exit():
    sys.exit(0)
  print("click: %d" % (j) )
  iterate()



# Takes a screenshot
#result = device.takeSnapshot()

# Output file image
#fileImage = os.path.join(os.path.dirname(os.sys.argv[0]), "shot1.png")

# Writes the screenshot to a file
#result.writeToFile(fileImage,'png')
