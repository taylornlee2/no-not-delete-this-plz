import random

choices = ['rock', 'paper', 'scissors']
comp = random.choice (choices)
user = raw_input(' Rock paper scissors shoot     ')
if user == 'rock' or 'paper' or 'scissors':
    print 'computer choice'
    print comp
if user == 'rock':
    if comp == 'rock':
        print 'Tie'
    elif comp == 'paper':
        print 'YOU SUCK'
    else:
        print 'Win'
if user == 'paper':
    if comp == 'rock':
        print 'Win'
    elif comp == 'paper':
        print 'Tie'
    else:
        print 'YOU SUCK'
if user == 'scissors':
    if comp == 'rock':
        print 'YOU SUCK'
    elif comp == 'paper':
        print 'Win'
    else:
        print 'Tie'