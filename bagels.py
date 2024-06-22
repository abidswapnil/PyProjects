# bagels.py

import random

class PyProject:
    def getSecretNum(self):
      MAX_DIGIT = 3
      return str(random.randrange(10**(MAX_DIGIT-1),10**(MAX_DIGIT))), MAX_DIGIT
    
    def getClues(self, sysGuess, userGuess):
      seen = set(sysGuess)
      res = ''
      
      for x, y in zip(sysGuess, userGuess):
        if x == y: res += 'Fermi '
        elif y in seen: res += 'Pico '
      
      if not res: print('Bagel')
      else: print(res)
      
    def bagels(self):
      NUM_GUESSES = 1
      MAX_GUESSES = 10
      sysGuess, MAX_DIGIT = self.getSecretNum()
      
      print(f"""I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
Pico         One digit is correct but in the wrong position.
Fermi        One digit is correct and in the right position.
Bagels       No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.""")
      
      while NUM_GUESSES <= MAX_GUESSES:
        userGuess = input(f'Guess #{NUM_GUESSES} - {sysGuess}: \n>')
        
        if len(userGuess) != MAX_DIGIT: continue
        elif userGuess == sysGuess:
          print("You got it!\nDo you want to play again? (yes or no)")
          if input('\n>').lower().startswith('n'): return "Thanks for playing!"
          else: self.bagels()
        else: self.getClues(sysGuess, userGuess)
          
        NUM_GUESSES += 1
        
      return "You ran out of guesses."
    

p = PyProject()
print(p.bagels())
