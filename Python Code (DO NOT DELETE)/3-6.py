import random

def generator():
    name = raw_input('name: ')
    num = random.randint(0,len(name)-1)
    print name[num]
    

def grade():
    grade= int(raw_input('What is your score'))
    print grade
    if 90 <= grade < 100:
        print("You received an A")
        
    elif 80 <= grade < 90:
        print("You received a B")

    elif 70 <= grade < 80:
        print("You received a C")

    elif 60 <= grade < 70:
        print("You received a D")
        
    elif 0 < grade < 60:
        print("You received a F")
    else:
        print('your wrong')
        