#!/usr/bin/env monkeyrunner
import sys, copy
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import eyes, monkey
from time import sleep

VERBOSE=False

def print_d(str):
  if VERBOSE:
    print str,

def println_d(str):
  if VERBOSE:
    print(str)

def print_table(t):
  print("_"*len(t)*6)
  for i in range(len(t)):
    print "|",
    for j in range(len(t[i])):
      if t[i][j] == 1:
        print " X  |",
      else:
        print "    |",
    print('')
  print("_"*len(t)*6)

class State:
  def __init__(self, table, moves):
    self.table = table
    self.moves = moves

  def move_down(self, i, j):
    if len(self.table) == i + 1:
      println_d("DOWN: last line")
      return False
    if self.table[i+1][j] == 1:
      println_d("DOWN: we have a neighbor")
      return False
    for ia in range(i+2,len(self.table)):
      if self.table[ia][j] == 1:
        println_d("DOWN: (%d,%d)->(%d,%d)" % (i,j,ia-1,j))
        sa = copy.deepcopy(self)
        sa.table[i][j] = 0
        sa.table[ia-1][j] = 1
        sa.moves.append(['D',(i,j)])
        sa.move_down_i(ia,j)
        return sa
    println_d("DOWN: ops.. no one found.")
    return False

  def move_down_i(self, i, j):
    print_d("DOWN_i: (%d,%d)->" % (i,j))
    if len(self.table) == i + 1:
      self.table[i][j] = 0
      println_d("out!")
      return
    for ia in range(i+1,len(self.table)):
      if self.table[ia][j] == 1:
        println_d("(%d,%d)" % (ia-1,j))
        self.table[i][j] = 0
        self.table[ia-1][j] = 1
        self.move_down_i(ia,j)
        return
    println_d("out!")
    self.table[i][j] = 0




  def move_right(self, i, j):
    if len(self.table[i]) == j + 1:
      println_d("RIGHT: last column")
      return False
    if self.table[i][j+1] == 1:
      println_d("RIGHT: we have a neighbor")
      return False
    for ja in range(j+2,len(self.table[i])):
      if self.table[i][ja] == 1:
        println_d("RIGHT: (%d,%d)->(%d,%d)" % (i,j,i,ja-1))
        sa = copy.deepcopy(self)
        sa.table[i][j] = 0
        sa.table[i][ja-1] = 1
        sa.moves.append(['R',(i,j)])
        sa.move_right_i(i,ja)
        return sa
    println_d("RIGHT: ops.. no one found.")
    return False

  def move_right_i(self, i, j):
    print_d("RIGHT_i: (%d,%d)->" % (i,j))
    if len(self.table[i]) == j + 1:
      self.table[i][j] = 0
      println_d("out!")
      return
    for ja in range(j+1,len(self.table[i])):
      if self.table[i][ja] == 1:
        println_d("(%d,%d)" % (i,ja-1))
        self.table[i][j] = 0
        self.table[i][ja-1] = 1
        self.move_right_i(i,ja)
        return
    println_d("out!")
    self.table[i][j] = 0



  def move_left(self, i, j):
    if j == 0:
      println_d("LEFT: last column")
      return False
    if self.table[i][j-1] == 1:
      println_d("LEFT: we have a neighbor")
      return False
    for ja in reversed(range(0, j-1)):
      if self.table[i][ja] == 1:
        println_d("LEFT: (%d,%d)->(%d,%d)" % (i,j,i,ja+1))
        sa = copy.deepcopy(self)
        sa.table[i][j] = 0
        sa.table[i][ja+1] = 1
        sa.moves.append(['L',(i,j)])
        sa.move_left_i(i,ja)
        return sa
    println_d("LEFT: ops.. no one found.")
    return False

  def move_left_i(self, i, j):
    print_d("LEFT_i: (%d,%d)->" % (i,j))
    if j == 0:
      self.table[i][j] = 0
      println_d("out!")
      return
    for ja in reversed(range(0,j)):
      if self.table[i][ja] == 1:
        println_d("(%d,%d)" % (i,ja+1))
        self.table[i][j] = 0
        self.table[i][ja+1] = 1
        self.move_right_i(i,ja)
        return
    println_d("out!")
    self.table[i][j] = 0



  def move_up(self, i, j):
    if i== 0:
      println_d("UP: last line")
      return False
    if self.table[i-1][j] == 1:
      println_d("UP: we have a neighbor")
      return False
    for ia in reversed(range(0, i-1)):
      if self.table[ia][j] == 1:
        println_d("UP: (%d,%d)->(%d,%d)" % (i,j,ia+1,j))
        sa = copy.deepcopy(self)
        sa.table[i][j] = 0
        sa.table[ia+1][j] = 1
        sa.moves.append(['U',(i,j)])
        sa.move_up_i(ia,j)
        return sa
    println_d("UP: ops.. no one found.")
    return False

  def move_up_i(self, i, j):
    print_d("UP_i: (%d,%d)->" % (i,j))
    if i == 0:
      self.table[i][j] = 0
      println_d("out!")
      return
    for ia in reversed(range(0,i)):
      if self.table[ia][j] == 1:
        println_d("(%d,%d)" % (ia+1,j))
        self.table[i][j] = 0
        self.table[ia+1][j] = 1
        self.move_up_i(ia,j)
        return
    println_d("out!")
    self.table[i][j] = 0



  def winner(self):
    balls = 0
    for line in self.table:
      for ball in line:
        if ball == 1:
          balls += 1

        if balls > 1:
          return False
    return True

  def next_states(self):
    states = []
    for i in range(len(self.table)):
      for j in range(len(self.table[i])):
        if self.table[i][j] == 1:
          println_d("found %d %d" % (i,j))
          # UP
          s = self.move_up(i,j)
          if s:
            if VERBOSE: print_table(s.table)
            states.append(s)
          # DOWN
          s = self.move_down(i,j)
          if s:
            if VERBOSE: print_table(s.table)
            states.append(s)
          # LEFT
          s = self.move_left(i,j)
          if s:
            if VERBOSE: print_table(s.table)
            states.append(s)
          # RIGHT
          s = self.move_right(i,j)
          if s:
            if VERBOSE: print_table(s.table)
            states.append(s)
    return states

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


if len(sys.argv) == 1:
  # Connects to the current device, returning a MonkeyDevice object
  device = MonkeyRunner.waitForConnection()

  # Takes a screenshot
  result = device.takeSnapshot()

  t = fling_eyes.load_table(result, True)
else:
  t = load_table(sys.argv[1])


s = State(t, [])

queue = Queue()
queue.put(s)

print_table(s.table)
print("\n\n\n")
winner_state = None
while not queue.empty():
  s = queue.get()
  if s.winner():
    winner_state = s
    print("WINNER!!_________")
    print_table(s.table)
    print(s.moves)
    print("/WINNER!!________")


  println_d("getting moves..._________")
  if VERBOSE: print_table(s.table)
  println_d("V________V")
  for sa in s.next_states():
    queue.put(sa)
  println_d("^________^")
  println_d("\n\n\n")


if len(sys.argv) == 1:
  for m in winner_state.moves:
    print(m)
    fling_monkey.move(device, m)
    sleep(1.5)
