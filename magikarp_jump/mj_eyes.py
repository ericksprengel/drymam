#!/usr/bin/env monkeyrunner
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import mj_device

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

def get_food_points(block):
  #pxf_min = [-1, 20, 35, 8]
  #pxf_max = [-1, 120, 159, 83]

  #MonkeyRunner.loadImageFromFile(imgFullPath)
  return mj_device.area.FOOD_SPAWN.slice(5,8)



def main(): 
  # Connects to the current device, returning a MonkeyDevice object
  device = MonkeyRunner.waitForConnection()

  # Takes a screenshot
  result = device.takeSnapshot()
  #result = MonkeyRunner.loadImageFromFile("res/full.png")


if __name__ == '__main__':
  main()

