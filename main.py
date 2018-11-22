from time import sleep
from sys import exit

class Game():
  def __init__(self):
    self.tilemap = [
      [0,0,0],
      [0,0,0],
      [0,0,0]
    ]
    self.step = 1
    
  def print(self):
    print(self.tilemap[0])
    print(self.tilemap[1])
    print(self.tilemap[2])
    
  def check(self, val):
    val0, val1 = int(val[0]), int(val[1])
    if self.tilemap[val0][val1] == 0:
      if self.step == 1:
        self.tilemap[val0][val1] = 1
        
      else:
        self.tilemap[val0][val1] = 2
        
      self.step = self.step * -1
      
    else: print("There is a {0} at that spot".format(self.tilemap[val0][val1]))
      
  def rules(self):
    for row in [0,1,2]:
      if self.tilemap[row][0] == self.tilemap[row][1] and self.tilemap[row][0] == self.tilemap[row][2]:
        if self.tilemap[row][0] != 0:
          self.winner(self.tilemap[row][0])
          
  def winner(self, win):
    print("The winner is player number {0}!".format(win))
    sleep(3)
    exit()
    
    
  def update(self):
    self.print()
    val = input("What is your choice?\n")
    self.check(val)
    self.rules()
    
ttt = Game()
    
while True:
  ttt.update()
