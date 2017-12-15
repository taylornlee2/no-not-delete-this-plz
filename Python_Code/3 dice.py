import random

def rolls ():
    counter = 1
    all_rolls = []
    while counter == 1:
        var1 = random.randint(1,6)
        var2 = random.randint(1,6)
        var3 = random.randint(1,6)
        
        all_rolls += [((var1 , var2, var3))]
        if var1 > var2 > var3 or var2 > var3 > var1 or var3 > var2 > var1 or var2 > var1 > var3 or var3 > var1 > var2 or var1 > var3 > var2:
            print (var1, var2, var3)
            print 'you win'
            gumbo = raw_input ('again  ')
            counter = 1
            if "yes or no":
                    if gumbo == 'yes':
                        counter = 1
                    if gumbo =='no':
                            counter = 0  
                    print (all_rolls)            
        else:
                    print (var1,var2,var3)
                    counter = 0
                    gumbo = raw_input ('again  ')
                    if "yes or no":
                        if gumbo =='yes':
                            counter = 1
                        if gumbo == 'no':
                                counter = 0
                    print all_rolls