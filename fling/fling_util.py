#!/usr/bin/env monkeyrunner
import sys, copy
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from Queue import Queue

def print_table(t):
  print("_"*len(t)*5 + "_")
  for i in range(len(t)):
    print "|",
    for j in range(len(t[i])):
      if t[i][j] == 1:
        print " X  |",
      else:
        print "    |",
    print('')
  print("_"*len(t)*5 + "_")


def load_table(file_path):
  f = open(file_path, "r")
  table = []
  for line in f.readlines():
    items = line.strip().split()
    tl = []
    for item in items:
      tl.append(int(item))
    table.append(tl)
  return table
