from __future__ import print_function # must be first in file
import random
 
def guess_once():
    secret = random.randint(1, 400000)
    print('I have a number between 1 and 400000.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        print('Wrong, my number is ', secret, '.', sep='')
    else:
        print('Right, my number is', guess, end='!\n')