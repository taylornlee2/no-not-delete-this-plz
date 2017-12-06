import matplotlib.pyplot as plt
import random

def roll():
    counter = 100
    all_rolls = []
    while counter >= 1:
        num = random.randint(1,6) + random.randint(1,6)
        all_rolls += [num]
        counter -= 1
  
        
    plt.hist(all_rolls)
    plt.show()

def dice():
    number = 0
    for num in range( int(raw_input('how many times do you want to roll?  '))):
        number += random.randint(1,6)
    print 'you got ' + str(number)