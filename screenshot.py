# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from time import sleep
import sys, os


# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
# device.installPackage('myproject/bin/MyApplication.apk')

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

# Takes a screenshot
result = device.takeSnapshot()

# Output file image
fileImage = os.path.join(os.path.dirname(os.sys.argv[0]), "shot1.png")

# Writes the screenshot to a file
result.writeToFile(fileImage,'png')
