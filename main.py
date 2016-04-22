#!/usr/bin/python
import copy
from Queue import Queue

def print_table(t):
  print "_"*len(t)*6
  for i in range(len(t)):
    print("|"),
    for j in range(len(t[i])):
      if t[i][j] == 1:
        print(" X  |"),
      else:
        print("    |"),
    print
  print "_"*len(t)*6

class State:
  def __init__(self, table, moves):
    self.table = table
    self.moves = moves

  def move_right(self, i, j):
    if len(self.table[i]) == j + 1:
      print("RIGHT: last column")
      return False
    if self.table[i][j+1] == 1:
      print("RIGHT: we have a neighbor")
      return False
    for ja in range(j+2,len(self.table[i])):
      if self.table[i][ja] == 1:
        print("RIGHT: ({0},{1})->({2},{3})".format(i,j,i,ja-1))
        sa = copy.deepcopy(self)
        sa.table[i][j] = 0
        sa.table[i][ja-1] = 1
        sa.moves.append(['R',(i,j)])
        sa.move_right_i(i,ja)
        return sa
    print("RIGHT: ops.. no one found.")
    return False

  def move_right_i(self, i, j):
    print("RIGHT_i: ({0},{1})->".format(i,j)),
    if len(self.table[i]) == j + 1:
      self.table[i][j] = 0
      print("out!")
      return
    for ja in range(j+1,len(self.table[i])):
      if self.table[i][ja] == 1:
        print("({0},{1})".format(i,ja-1))
        self.table[i][j] = 0
        self.table[i][ja-1] = 1
        self.move_right_i(i,ja)
        return
    print("out!")
    self.table[i][j] = 0



  def move_left(self, i, j):
    if j == 0:
      print("LEFT: last column")
      return False
    if self.table[i][j-1] == 1:
      print("LEFT: we have a neighbor")
      return False
    for ja in reversed(range(0, j-2)):
      if self.table[i][ja] == 1:
        print("LEFT: ({0},{1})->({2},{3})".format(i,j,i,ja+1))
        sa = copy.deepcopy(self)
        sa.table[i][j] = 0
        sa.table[i][ja+1] = 1
        sa.moves.append(['L',(i,j)])
        sa.move_left_i(i,ja)
        return sa
    print("LEFT: ops.. no one found.")
    return False

  def move_left_i(self, i, j):
    print("LEFT_i: ({0},{1})->".format(i,j)),
    if j == 0:
      self.table[i][j] = 0
      print("out!")
      return
    for ja in reversed(range(0,j-1)):
      if self.table[i][ja] == 1:
        print("({0},{1})".format(i,ja+1))
        self.table[i][j] = 0
        self.table[i][ja+1] = 1
        self.move_right_i(i,ja)
        return
    print("out!")
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
          print("found {0} {1}".format(i,j))
          #s = self.move_up()
          #s = self.move_down()
          #s = self.move_left()
          s = self.move_left(i,j)
          if s:
            print_table(s.table)
            states.append(s)
          s = self.move_right(i,j)
          if s:
            print_table(s.table)
            states.append(s)
    return states


t = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,0,0,1],
    [0,0,0,0,0],
  ]
s = State(t, [])

queue = Queue()
queue.put(s)

print_table(s.table)
print("\n\n\n")
while not queue.empty():
  s = queue.get()
  if s.winner():
    print("WINNER!!_________")
#    print_table(s.table)
    print(s.moves)
#    print("/WINNER!!________")

  
  print("getting moves..._________")
  print_table(s.table)
  print("V________V")
  for sa in s.next_states():
    queue.put(sa)
  print("^________^")
  print("\n\n\n")
