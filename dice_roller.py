# Dice roller
# Author: Abid

import random
class PyProject:
  def dice_roller(self):
    inp = input('>').strip()
    
    # splitting notations into no. of dice, no. of side of dice, bonus
    notations = []
    i, symb = -1, None
    
    for j in range(len(inp)):
      if inp[j] in ['d', '+', '-']:
        notations.append(int(inp[i+1:j]))
        i = j
        symb = inp[j] if inp[j] in ['+', '-'] else ''
    notations.append(int(symb + inp[i+1:j+1]))
    
    res = []
    
    for _ in range(notations[0]):
      res.append(random.randrange(1, notations[1]))
    
    if symb in ['+', '-']: res.append(notations[-1])
    return tuple(res)
  
p = PyProject()
print(p.dice_roller())