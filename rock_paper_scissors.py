# Rock paper scissors
# Author: Abid

import time
import random
class PyProject:
  def wait(self, move):
    # hashmap to store win move against user move
    gmap = {'P':['PAPER', 'ROCK'], 'R':['ROCK', 'SCISSORS'], 'S':['SCISSORS', 'PAPER']}
    
    user_move, win_move = gmap[move]
    
    print(f'{user_move} versus...')
    for i in range(3):
      print(f'{i+1}...')
      time.sleep(1)
    
    # hashmap for mapping number ranging from 1 to 3 with particular move
    hmap = {1:'ROCK', 2: 'PAPER', 3: 'SCISSORS'}
    
    # storing system move
    sys_move = hmap[random.randrange(1,4)]
    
    
    if sys_move == win_move:
      print(f'{sys_move}\nYou win!')
      return 2
    elif sys_move == user_move:
      print(f'{sys_move}\nTie!')
      return 0
    else:
      print(f'{sys_move}\nYou lose!')
      return 1
    
  def rock_paper_scissor(self, win, loss, tie):
    
    while True:
      move = input(f'{win} Wins, {loss} Losses, {tie} Ties \n'
                   f'Enter your move: (R)ock (P)aper (S)cissors or (Q)uit \n>').upper()
      if move.upper().startswith('Q'): return ''
      
      try:
        result = self.wait(move)
        if result == 0: tie += 1
        elif result == 1: loss += 1
        elif result == 2: win += 1
        
      except KeyError: continue
      
      
p = PyProject()
print(p.rock_paper_scissor(0, 0, 0))