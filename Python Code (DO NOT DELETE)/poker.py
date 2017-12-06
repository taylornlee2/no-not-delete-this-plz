import random

def poker():
    p1 = []
    p2 = [[]]
    
    counter = 0 
    while True :
        p1 += [str(cards) + str(suit)]
        p2 += [str(cards) + str(suit)]
        counter +=1
        print p1
        print p2
        if counter > 4:
            break
    
def cards():
    player1 = random.randint(1,13)
    player2 = random.randint(1,13)
      
def randomcard():
    card = random.randint(1,13)

def suit():
    suit_list = ('H','S','D','C') 

def cardtoface():
    if card == 1:
        card = 'A'
    elif card == 11:
        card = "J"
    elif card == 12:
        card = "Q"
    elif card == 13:
        card = "K"
    return card


   
      
    
