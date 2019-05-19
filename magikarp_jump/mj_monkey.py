#!/usr/bin/env monkeyrunner
import sys, copy
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import random

def drag(device, drag, msg=None, debug=False):
  if msg:   print(msg)
  if debug: print(drag)
  device.drag(
      (drag.p0.x, drag.p0.y),
      (drag.p1.x, drag.p1.y),
      drag.t, drag.steps)

def touch(device, point, sleep=None):
  if not sleep: sleep = random.random()/10 + 0.1 # 0.1s ~ 0.2s
  device.touch(point.x,point.y,MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(sleep)

def touch_area(device, area, sleep, debug=False):
  point = Point(
      random.randint(area.p0.x, area.p1.x),
      random.randint(area.p0.y, area.p1.y)
    )
  if debug:
    now = datetime.datetime.now()
    # http://bugs.jython.org/issue2166
    #save_screenshot(device, "%s_%s_%s.png" % (now.strftime("%y-%m-%d_%H-%M"), now.microsecond, area[2]))
    print("click: %s, %s\t\t%s" % (tap[0], tap[1], area[2]) )
  device.touch(point.x, point.y, MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(sleep)

def sleep(delay):
  MonkeyRunner.sleep(delay)

def main():
  # Connects to the current device, returning a MonkeyDevice object
  device = MonkeyRunner.waitForConnection()


if __name__ == '__main__':
  main()
