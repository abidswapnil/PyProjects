# rock_paper_scissors(always-win).py
# Author: Abid

import time
class PyProject:
  def wait(self, user_move):
    # hashmap to store wrong move against user input
    hmap = {'P': ['PAPER', 'ROCK'], 'R': ['ROCK', 'SCISSORS'], 'S':['SCISSORS', 'PAPER']}
    
    print(f'{hmap[user_move][0]} versus...')
    for i in range(3):
      print(f'{i+1}...')
      time.sleep(1)
      
    print(f'{hmap[user_move][1]} \nYou win!')
  def rock_paper_scissor(self):
    win, loss, tie = 0, 0, 0
    
    while True:
      inp = input(f'{win} Wins, {loss} Losses, {tie} Ties \nEnter your move: (R)ock (P)aper (S)cissors or (Q)uit \n>').upper()
      if inp.upper().startswith('Q'): return ''
      
      try: self.wait(inp)
      except KeyError: continue
      
      win += 1
      
p = PyProject()
print(p.rock_paper_scissor())