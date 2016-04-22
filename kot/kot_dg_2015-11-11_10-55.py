# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys, os
import random

class areas:
  GOLD      = ((900, 560),(1000, 700))
  RESTART   = ((110,1000),( 140,1023))


# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

def get_tap_on_gold():
  return (
      random.randint(areas.GOLD[0][0], areas.GOLD[1][0]),
      random.randint(areas.GOLD[0][1], areas.GOLD[1][1])
    )

def get_tap_on_restart():
  return (
      random.randint(areas.RESTART[0][0], areas.RESTART[1][0]),
      random.randint(areas.RESTART[0][1], areas.RESTART[1][1])
    )

def is_there_restart():
  si = device.takeSnapshot().getSubImage( (85, 1020, 200, 200) )
  si.writeToFile("si.png", "png")
  print(device.takeSnapshot().getRawPixel(85, 1020))
#  if 85,1020 == rgb(253,45,46)
  return False

def iterate(time=0):
  tap = get_tap_on_gold()
  print("  click: %s" % (tap,) )
  print("  time: %s" % time )

  ts= [ 0.105, 0.05 ]

  for t in ts:
    print("  t: %s" % t )


  # start
  device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)

  for t in ts:
    MonkeyRunner.sleep(t)
    device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
    print(t)

  # # 2nd trap (spinner)
  # MonkeyRunner.sleep(1.25)
  # device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
  # MonkeyRunner.sleep(0.5)

  # # 3nd trap (out of whole)
  # device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
  # MonkeyRunner.sleep(0.2)
  # device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
  # MonkeyRunner.sleep(0.5)
  # device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)

  # # 4nd trap (final up)
  # MonkeyRunner.sleep(3.5)
  # # to left
  # device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)
  # MonkeyRunner.sleep(0.2)
  # device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)

  # # to right
  # MonkeyRunner.sleep(0.5)
  # device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)

  # # to left
  # MonkeyRunner.sleep(1.1)
  # device.touch(tap[0],tap[1],MonkeyDevice.DOWN_AND_UP)


  MonkeyRunner.sleep(2.0)

  # if is_there_restart():
  #   restart_tap = get_tap_on_restart()
  #   device.touch(restart_tap[0], restart_tap[1], MonkeyDevice.DOWN_AND_UP)

  

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
  iterate(j)



# Takes a screenshot
#result = device.takeSnapshot()

# Output file image
#fileImage = os.path.join(os.path.dirname(os.sys.argv[0]), "shot1.png")

# Writes the screenshot to a file
#result.writeToFile(fileImage,'png')
