#!/usr/bin/env monkeyrunner
from mj_util import Point
from mj_util import Area
from mj_util import Drag

class area:
  FOOD_SPAWN = Area(Point(  50,  315), Point(680, 970))
  TRAINING_BUTTON = Area(Point( 250,  1100), Point(490, 1150))


# start The starting point of the drag gesture, in the form of a tuple (x,y) where x and y are integers.
# end The end point of the drag gesture, in the form of a tuple (x,y) where x and y are integers.
# duration  The duration of the drag gesture in seconds. The default is 1.0 seconds.
# steps The number of steps to take when interpolating points. The default is 10.
class drag:
  MOVE_TO_RIGHT_FOOD_SPAWN = Drag(
      Point(area.FOOD_SPAWN.p0.x, area.FOOD_SPAWN.get_center().y),
      Point(area.FOOD_SPAWN.p1.x, area.FOOD_SPAWN.get_center().y),
      1.0)
  MOVE_TO_LEFT_FOOD_SPAWN = Drag(
      Point(area.FOOD_SPAWN.p1.x, area.FOOD_SPAWN.get_center().y),
      Point(area.FOOD_SPAWN.p0.x, area.FOOD_SPAWN.get_center().y),
      1.0)
  DEEP_TO_FOOD_SPAWN = Drag(
      Point(area.FOOD_SPAWN.get_center().x, area.FOOD_SPAWN.p1.y),
      Point(area.FOOD_SPAWN.get_center().x, area.FOOD_SPAWN.p0.y),
      1.0)

def main():
  print("TODO")

if __name__ == '__main__':
  main()

