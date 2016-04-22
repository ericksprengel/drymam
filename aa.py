# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys, os
import datetime
import random

SANDBOX_AREA = ( (110,280), (650,1000) )

class buttons:
  UP_WORLD      = (665,  200)
  DOWN_WORLD    = (665, 1080)
  MARTIAN_WORLD = (665,  965)

class colors:
  BOX_BROWN = (-1, 192, 142,  87)
  COW_WHITE = (-1, 254, 254, 254)

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
# device.installPackage('myproject/bin/MyApplication.apk')

# sets a variable with the package's internal name
package = 'br.com.tapps.cowevolution'

# sets a variable with the name of an Activity in the package
activity = 'com.ansca.corona.CoronaActivity'

# sets the name of the component to start
runComponent = package + '/' + activity

# Runs the component
device.startActivity(component=runComponent)

def takeSnapshot():
  # Takes a screenshot
  image = device.takeSnapshot()

  # Output file image
  filename = "shot.png"
#  filename = "shot-%s.png" % datetime.datetime.now().strftime("%Y-%m-%d_%H-%M_%f")
  fileImage = os.path.join(os.path.dirname(os.sys.argv[0]), filename)

  # Writes the screenshot to a file
  image.writeToFile(fileImage,'png')
  return image

def wait_for_nice_button():
  #310, 810 -> 330, 840
  #rgb 146,234,89
  return False

def find_boxes(image):
  boxes = []
  d = 30
  for xp in range( SANDBOX_AREA[0][0]/d, SANDBOX_AREA[1][0]/d):
    x = xp*d
    for yp in range(SANDBOX_AREA[0][1]/d, SANDBOX_AREA[1][1]/d):
      y = yp*d
      if image.getRawPixel(x,y) == colors.BOX_BROWN:
        boxes.append((x,y))   
  return boxes

def find_cows(image):
  cows = []
  d = 30
  for xp in range( SANDBOX_AREA[0][0]/d, SANDBOX_AREA[1][0]/d):
    x = xp*d
    for yp in range(SANDBOX_AREA[0][1]/d, SANDBOX_AREA[1][1]/d):
      y = yp*d
      if image.getRawPixel(x,y)[1] == 254:
        cows.append((x,y))   
  return cows

#def remove_nears(points, image, d):
#  d = int(distance*2.5)
#  result = []
#  for xp in range( SANDBOX_AREA[0][0]/d + 2, SANDBOX_AREA[1][0]/d + 2):
#    x = xp*d
#    for yp in range(SANDBOX_AREA[0][1]/d + 2, SANDBOX_AREA[1][1]/d):
#      y = yp*d
#      cluster = []
#      for idx, p in enumerate(points):
#        dx = p[0] - x
#        dy = p[1] - y
#        if dx*dx + dy*dy <= distance*distance:
#          cluster.append(p)
#      #select one of the cluster points
#      if len(cluster) > 0:
#        result.append(random.choice(cluster))
#  return result


def iterate(open_boxes=True):
  image = takeSnapshot()
  
  if open_boxes:
    # BOXES
    print("boxes...")
    boxes = find_boxes(image)
    print(len(boxes))
    for box in boxes:
      print("box: %s" % (box,) )
      device.touch(box[0],box[1],MonkeyDevice.DOWN_AND_UP)
#      MonkeyRunner.sleep(0.2)
  
  # COWS
  print("cows...")
  cows = find_cows(image)
  random.shuffle(cows)
  print(len(cows))
  for cow in cows:
    print("cow: %s" % (cow,) )
    device.touch(cow[0],cow[1],MonkeyDevice.DOWN_AND_UP)
#    sleep(0.1)
    device.drag(cow,(400,750), 1.0 ,10)
  
# Presses the Menu button
# device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

counter = 0
#while True:
for j in range(1):
  for i in range(6):
    print("Earth 0 iteration %d,%d" % (i,j))
    iterate(True)
  device.touch(buttons.UP_WORLD[0],buttons.UP_WORLD[1],MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(2.0)
  for i in range(2):
    print("Earth 1 iteration %d,%d" % (i,j))
    iterate(False)
  device.touch(buttons.DOWN_WORLD[0],buttons.DOWN_WORLD[1],MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(2.0)



# Takes a screenshot
#result = device.takeSnapshot()

# Output file image
#fileImage = os.path.join(os.path.dirname(os.sys.argv[0]), "shot1.png")

# Writes the screenshot to a file
#result.writeToFile(fileImage,'png')
