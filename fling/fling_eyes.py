#!/usr/bin/env monkeyrunner
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import fling_util

def get_min_max_in_block(block):
  px_min = [-1, 256, 256, 256]
  px_max = [-1,  -1,  -1,  -1]

  for x in range(10):
    for y in range(10):
      px = block.getRawPixel(x,y)
      for c in range(0,4):
        if px[c] < px_min[c]:
          px_min[c] = px[c]
        elif px[c] > px_max[c]:
          px_max[c] = px[c]
  return {"min": px_min, "max": px_max}

def get_min_max(image, dump=False):

  px_min = [-1, 255, 255, 255]
  px_max = [-1,   0,   0,   0]
  for i in range(8):
    for j in range(7):
      x = j*102 + 0    + 102/4
      y = i*112 + 173  + 112/4
      width  = 102/2
      height = 112/2
      block = image.getSubImage((x,y,width,height))

      if dump: # dump blocks
        fpath = 'res/block_%d_%d.png' % (i,j)
        block.writeToFile(fpath, 'png')
        print(fpath)


      res = get_min_max_in_block(block)
      for c in range(0,4):
        if res["min"][c] < px_min[c]:
          px_min[c] = res["min"][c]
        else:
          px_max[c] = res["max"][c]
  

  print("_____")
  print("min: %s" % str(px_min))
  print("max: %s" % str(px_max))

def is_empty_block(block):
  pxf_min = [-1, 20, 35, 8]
  pxf_max = [-1, 120, 159, 83]

  for x in range(10):
    for y in range(10):
      px = block.getRawPixel(x,y)
      for c in range(1,4):
        if px[c] < pxf_min[c] or px[c] > pxf_max[c]:
          print(get_min_max_in_block(block))
          return False
  return True


def get_empty_table():
  table = []
  for i in range(8):
    table.append([])
    for j in range(7):
      table[i].append(None)
  return table

def load_table(image, dump=False):
  # getting a sub image from snapshot?
  table = get_empty_table()
  for i in range(8):
    for j in range(7):
      x = j*102 + 0    + 102/4
      y = i*112 + 173  + 112/4
      width  = 102/2
      height = 112/2
      block = image.getSubImage((x,y,width,height))

      if dump: # dump blocks
        fpath = 'res/block_%d_%d.png' % (i,j)
        block.writeToFile(fpath, 'png')
        print(fpath)

      if is_empty_block(block):
        table[i][j] = 0
      else:
        table[i][j] = 1

  return table


def main(): 
  # Connects to the current device, returning a MonkeyDevice object
  device = MonkeyRunner.waitForConnection()

  # Takes a screenshot
  result = device.takeSnapshot()
  #result = MonkeyRunner.loadImageFromFile("res/full.png")

  fling_util.print_table(load_table(result, True))


if __name__ == '__main__':
  main()

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

