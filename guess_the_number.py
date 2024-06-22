# guess_the_number.py
# Author: Abid

class PyProject:
  def guess_the_number(self):
    import random
    
    # generating a random number in between range (1, 100)
    num = random.randrange(1, 100)
    
    # number of times user can guess at max
    numGuess = 10
    
    print('I am thinking of a number between 1 and 100.')
    while numGuess:
      # taking input from user
      inp = int(input(f"You have {numGuess} guesses left. Take a guess. \n >"))
      
      # matching the random number with the user given number
      if inp == num: return "Yay! You guessed the number."
      elif inp < num: print('Your guess is too low.')
      else: print('Your guess is too high.')
      
      numGuess -= 1

p = PyProject()
print(p.guess_the_number())


