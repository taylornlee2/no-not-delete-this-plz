def hangman2():
    secret = raw_input("put a word here  ")
    while True:
        guess = raw_input('keep guessing   ')
        result = ''
        if guess == secret:
                print 'you win'
                break
        for i in range(len(secret)):
            for letter in guess:
                print (letter)        
                if letter == secret[i]:
                    result += letter
                else:
                    result += '-'
                    print ('R:' + result)
 