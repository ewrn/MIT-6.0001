# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed = 0
    
    for letter in secret_word:
        if letter in letters_guessed:
            guessed += 1
            
    return guessed == len(secret_word)

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word += letter
        else:
            word += "_ "

    return word
    
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = ""
    for letter in string.ascii_lowercase:
        if letter in letters_guessed:
            continue
        all_letters += letter
    
    return all_letters

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    score = 0
    guesses = 6
    warnings = 3 
    letters_guessed = []
    word_guessed = get_guessed_word(secret_word, letters_guessed)
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings, "warnings left.")
    
    while guesses != 0 and word_guessed != secret_word:
        print("-------------")
        
        if guesses == 1:
            print("You have", guesses, "guess left.")
        else:
            print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        
        
        make_guess = input("Please guess a letter:")
        make_guess = str.lower(make_guess)
        
        if not str.isalpha(make_guess) or len(make_guess) != 1:
            if warnings == 0:
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", word_guessed)
                guesses -= 1
            else:
                warnings -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:", word_guessed)
            continue
        elif make_guess in letters_guessed:
            if warnings == 0:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", word_guessed)
                guesses -= 1
            else:
                warnings -= 1
                print("Oops! You've already guessed that letter. You have", warnings, "warnings left:", word_guessed)
            continue
        elif str.isalpha(make_guess) and len(make_guess) == 1:
            letters_guessed.append(make_guess)

        if make_guess in secret_word:
            word_guessed = get_guessed_word(secret_word, letters_guessed)
            print("Good guess:", word_guessed)
        else:
            if make_guess in "aeiou":
                guesses -= 2
            else:
                guesses -= 1
            print("Oops! That letter is not in my word:", word_guessed)
            
    score = len(set(word_guessed)) * guesses
    
    print("-------------")
    if word_guessed == secret_word:
        print("Congratulations, you won!")
        print("Your total score for this game is:", score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    unknown_letters = []
    known_letters = []
    
    if len(my_word) != len(other_word):
        return False
    
    for x in range(len(my_word)):
        if my_word[x] == "_":
            unknown_letters.append(other_word[x])
            if other_word[x] in known_letters:
                return False
        else:
            known_letters.append(my_word[x])
            if my_word[x] != other_word[x] or my_word[x] in unknown_letters:
                return False            
    return True
    
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    to_print = ""
    for string in wordlist:
        if match_with_gaps(my_word, string):
            to_print += string + " "
    if to_print == "":
        print("No matches found")
    else:
        print(to_print)

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    score = 0
    guesses = 6
    warnings = 3 
    letters_guessed = []
    word_guessed = get_guessed_word(secret_word, letters_guessed)
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings, "warnings left.")
    
    while guesses != 0 and word_guessed != secret_word:
        print("-------------")
        
        if guesses == 1:
            print("You have", guesses, "guess left.")
        else:
            print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        
        
        make_guess = input("Please guess a letter:")
        make_guess = str.lower(make_guess)
        
        if make_guess == "*":
            print("Possible word matches are:")
            show_possible_matches(word_guessed)
            continue
        
        if not str.isalpha(make_guess) or len(make_guess) != 1:
            if warnings == 0:
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", word_guessed)
                guesses -= 1
            else:
                warnings -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:", word_guessed)
            continue
        elif make_guess in letters_guessed:
            if warnings == 0:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", word_guessed)
                guesses -= 1
            else:
                warnings -= 1
                print("Oops! You've already guessed that letter. You have", warnings, "warnings left:", word_guessed)
            continue
        elif str.isalpha(make_guess) and len(make_guess) == 1:
            letters_guessed.append(make_guess)

        if make_guess in secret_word:
            word_guessed = get_guessed_word(secret_word, letters_guessed)
            print("Good guess:", word_guessed)
        else:
            if make_guess in "aeiou":
                guesses -= 2
            else:
                guesses -= 1
            print("Oops! That letter is not in my word:", word_guessed)
            
    score = len(set(word_guessed)) * guesses
    
    print("-------------")
    if word_guessed == secret_word:
        print("Congratulations, you won!")
        print("Your total score for this game is:", score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word, ".")

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)