
# ----------------
# Project: Encryption

# Skills used: for loops, while loops, functions, String/list operations, module import, Dictionaries, Assertions/Exceptions, Classes/Inheritance, getter/setter
# ----------------

# -----------------------------------
# Helper code (Provided by the course MITx 6.00.1x)

import string

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
WORDLIST_FILENAME = 'words.txt'

# -----------------------------------
# Helper code (Provided by the course MITx 6.00.1x)
# Predefined class Message object
class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

# end of helper code
# -----------------------------------
         

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # initialize a "shifted" dictionary
        dic = {}
        
        # upperletters and lowerletters, all of the valid letters
        upperletters= string.ascii_uppercase
        lowerletters= string.ascii_lowercase
        
        # i is shift
        i = shift
        
        # loop through each letter in upperletters
        for letter in upperletters:
            # set an "index" variable to the lowercase letter position, use % 26 to "flip" the number
            shiftto=(upperletters.index(letter)+i)%26
            # add the shiftto upperletters the "shifted" dictionary
            dic[letter]=upperletters[shiftto]  
            
        # loop through each letter in lowerletters
        for letter in lowerletters:
            # set an "index" variable to the lowercase letter position, use % 26 to "flip" the number
            shifttolow=((lowerletters.index(letter)+i)%26)
            # continue add the shiftto lowerletters the "shifted" dictionary
            dic[letter]=lowerletters[shifttolow]
        
        # return "shifted" dictionary
        return dic


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # create a variable dic to be a dictionary using build_shift_dicton "shift"
        dic = self.build_shift_dict(shift)
        
        # initialize a shift_dict string variable
        shift_dict= ""
        
        # loop through each character in get_message_text 
        for i in self.get_message_text():
            # if the character is in the shifted dictionary
            if i in dic:
                # add the shifted character to the shift_dict(dic[i])
                shift_dict+= dic[i]
            # otherwise, add the character to the shift_dict
            else:
                shift_dict+= i
                
        # return result     
        return shift_dict
    
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        # set the instance variable Message text
        Message.__init__(self, text)
        
        # set the instance variable "shift" to the shift
        self.shift = shift
        # set the instance variable "encrypting_dict" to the instance method "build_shift_dict" applied to "shift"
        self.encrypting_dict = self.build_shift_dict(self.shift)
        # set the instance variable "message_text_encrypted" to the instance method "apply_shift" applied to "shift"
        self.message_text_encrypted = self.apply_shift(self.shift)


    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        # get shift
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        # get encrypting_dict
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        # get message_text_encrypted
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        # set the instance variable "shift" to the shift
        self.shift = shift
        # set the instance variable "encrypting_dict" to the instance method "build_shift_dict" applied to "shift"       
        self.encrypting_dict = self.build_shift_dict(self.shift)
        # set the instance variable "message_text_encrypted" to the instance method "apply_shift" applied to "shift"
        self.message_text_encrypted = self.apply_shift(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # set the instance variable Message text
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        # Set a variable for the maximum
        maximum = 0
        # Set a variable for the best
        best = 0
        # Set variable "valid_words" to the load_wordsfunction applied to the WORDLIST_FILENAME
        word_list= self.get_valid_words()
        
        # Test all possibilities (26 letters)
        for s in range(26):
            # try shift it
            text = self.apply_shift(s)
            # split it
            textlist = text.split(" ")
            # reset the score
            score=0
            
            # check thru all words
            for word in textlist:
                # if it is valid, add one to the score card
                if is_word(word_list, word) == True:
                    score += 1
            # if score greater than the maximum
            if score > maximum:
                # maximum is score
                maximum = score
                # s is the best possibility
                best = s
        
        # return the best guess and result
        return (best, self.apply_shift(best))


# Test Case 5-1:
plaintext = PlaintextMessage('hello', 2)
# print('Expected Output: jgnnq')
# print('Actual Output:', plaintext.get_message_text_encrypted())
    
# Test Case 5-2:
ciphertext = CiphertextMessage('jgnnq jgnnq')
# print('Expected Output:', (24, 'hello'))
# print('Actual Output:', ciphertext.decrypt_message())

story = get_story_string()
thestory = CiphertextMessage(story)
thestory = thestory.decrypt_message()
thestory = thestory[1]
print (thestory)



