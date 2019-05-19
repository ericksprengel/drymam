#!/usr/bin/env monkeyrunner
import sys, copy
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from Queue import Queue
import math

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def distance(self, p):
    return math.sqrt(
        math.pow(self.x - p.x, 2)
      + math.pow(self.y - p.y, 2))

  def __repr__(self):
    return str((self.x, self.y))

class Area:
  def __init__(self, p0, p1):
    self.p0 = p0
    self.p1 = p1

  def get_center(self):
    return Point(
        (self.p0.x + self.p1.x)/2,
        (self.p0.y + self.p1.y)/2)

  def slice(self, rows, columns):
    width  = (self.p1.x - self.p0.x)/(columns)
    height = (self.p1.y - self.p0.y)/(rows)

    x0 = self.p0.x +  width/2
    y0 = self.p0.y + height/2

    points = []
    for i in range(rows):
      for j in range(columns):
        x = j*width  + x0
        y = i*height + y0
        points.append(Point(x,y))
    return points


class Drag:
  def __init__(self, p0, p1, t, steps=None):
    self.p0 = p0
    self.p1 = p1
    self.t  = t
    if steps:
      self.steps = steps
    else:
      self.steps = int(t*50*1000/p0.distance(p1))

  def __repr__(self):
    return str((self.p0, self.p1, self.t, self.steps))

