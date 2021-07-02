
# ----------------
# Project: Hangman game

# Skills used: for loops, while loops, functions, String/list operations, module import
# ----------------


# -----------------------------------
# Helper code (Provided by the course MITx 6.00.1x)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()



def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN CODE HERE...
    
    # looping thru each letter in secretWord
    for letters in secretWord:
        
        # if any letter is not in lettersGuessed, return False
        if letters  not in lettersGuessed:
            return False

    # if all passed, return True            
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN CODE HERE...
    
    # create a empty string for storing the return prompt
    newsecretWord = ""
    
    # looping thru secretWord, if the letters guessed, replace and concatenate with underscore
    for letters in secretWord:
        if letters not in lettersGuessed:
            newsecretWord = newsecretWord +"_ "
        else:
            newsecretWord = newsecretWord + letters
            
    # return prompt            
    return newsecretWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN CODE HERE...
    
    # get a list of lowercase letters
    import string
    reminding = list(string.ascii_lowercase)
    
    # loooping thru lettersGuessed and remove it from reminding letters
    for i in lettersGuessed:
        reminding.remove(i)

    # turn a list of characters into a string
    return  ''.join(reminding)    


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN CODE HERE...

    #--- At the start of the game, let the user know how many 
    #--- letters the secretWord contains.
    
    # print greeting texts:
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is",len(secretWord),"letters long.")

    # get a list of lowercase letters
    import string
    availableLetters = string.ascii_lowercase    
    # set available mistakesMade to 8
    mistakesMade = 8
    # set lettersGuessed as an empty list
    lettersGuessed = []
    
    #--- After each round, you should also display to the user the 
    #--- partially guessed word so far, as well as letters that the 
    #--- user has not yet guessed.
    
    # while loop when available mistakesMade greater than 0
    while mistakesMade > 0 :
        
        # reset availableLetters to the most updated getAvailableLetters function's return
        availableLetters = getAvailableLetters(lettersGuessed)

        # spacing out and print greeting texts
        print ("-------------")
        print("You have",mistakesMade,"guesses left.")
        print("Available letters:", availableLetters)
        
        #--- Ask the user to supply one guess (i.e. letter) per round.
        
        # ask for new input
        guess = input("Please guess a letter: ") 
        # make sure the input is set to lowercase
        guessInLowerCase = guess.lower()

        #--- The user should receive feedback immediately after each guess 
        #--- about whether their guess appears in the computers word.
        
        # check if this is a guessed letter        
        if guessInLowerCase in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        # if not, append the guessed letter        
        else:            
            lettersGuessed.append(guessInLowerCase)
            # if guessInLowerCase is in the secretWord
            if guessInLowerCase in secretWord:
                # print reminding prompt
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
                # if the whole word guessed, break
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    break

            # if guessInLowerCase is NOT in the secretWord
            else:
                # reduce available mistakesMade by 1
                mistakesMade -=1
                # print mistake text
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))


    # break out of the while loop
    # when no more available mistakesMade
    # or whole word guessed
    # check and print accordingly
    print ("-------------")
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print("Congratulations, you won!")
    else:
        print ("Sorry, you ran out of guesses. The word was", secretWord + ".")



# Test Case 1-1:
secretWord = "apple"
hangman(secretWord)

# Test Case 1-2:
# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)