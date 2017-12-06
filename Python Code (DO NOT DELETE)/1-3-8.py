from __future__ import print_function
import random
 
def guess():
    secret = random.randint(1, 20)   
    print('I have a number between 1 and 20.')
    while True:  
        guess = int(raw_input('Guess: '))
        if guess != secret:
            print('Wrong, not my number')
            if guess > secret:
                print ('too high')
            if guess < secret:
                print ('too low')
        else:
            print('Right, my number is', guess, end='!\n')
            break