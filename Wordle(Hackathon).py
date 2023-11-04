import random as rnd
def getGuess(num):
    guess = input('Insert Guess #' + str(num + 1) + '/6: ')
    while not(len(guess)==5):
        guess = input('Your guess must be 5 letters! Try again: ')
    return guess

def checkLetter(index,letter,word):
    if letter == word[index]:
        return 1
    elif letter in word:
        return 2
    else:
        return 3

def checkWord(currentGuess,currentWord):
    out = ''
    for index in range(len(currentGuess)):
        result = checkLetter(index,currentGuess[index],currentWord)
        if result == 1:
            out += str(currentGuess[index]) + ': Correct. \n'
        elif result == 2:
            out += str(currentGuess[index]) + ': Wrong spot. \n'
        elif result == 3:
            out += str(currentGuess[index]) + ': Incorrect. \n'
    return out

words = ['peril','relay','relax','ridge','pause','paste','arson','scrap','hotel','motel','blame','beast','eagle','bound','audio','cough','blind','clean','drive','rinse','clues','weary','vague','climb','germs','blade','manic','tapir',]

currentWord = rnd.choice(words)
for x in range(6):
    currentGuess = getGuess(x)
    if currentGuess == currentWord:
        if x == 0:
            print('Correct! The word was ' + currentWord + '. You got it in ' + str(x+1) + ' guess!')
        else:
            print('Correct! The word was ' + currentWord + '. You got it in ' + str(x+1) + ' guesses!')
        break
    else:
        print(checkWord(currentGuess,currentWord))
        print('----------------------------------------')
    if x == 5:
        print('You Lose! The word was ' + currentWord + '.')
                
