# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys, os
import random

class areas:
  GOLD      = ((900,560),(1000, 700))


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

  # start
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)

  # 1st trap (red guard)
  MonkeyRunner.sleep(0.1)
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(0.77899)
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)

  # 2nd trap (spinner)
  MonkeyRunner.sleep(1.25)
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(0.5)

  # 3nd trap (out of whole)
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(0.2)
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(0.5)
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)

  # 4nd trap (final up)
  MonkeyRunner.sleep(3.5)
  # to left
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(0.2)
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)

  # to right
  MonkeyRunner.sleep(0.5)
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)

  # to left
  MonkeyRunner.sleep(1.1)
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)

  MonkeyRunner.sleep(4.0)
  

def must_exit():
  f = open('must_exit', 'r')
  request = f.read()
  f.close()
  print(request)
  return request.strip() == "1"

counter = 0
#while True:
for j in range(10):
  if must_exit():
    sys.exit(0)
  print("iteration: %d" % (j) )
  iterate()



# Takes a screenshot
#result = device.takeSnapshot()

# Output file image
#fileImage = os.path.join(os.path.dirname(os.sys.argv[0]), "shot1.png")

# Writes the screenshot to a file
#result.writeToFile(fileImage,'png')
