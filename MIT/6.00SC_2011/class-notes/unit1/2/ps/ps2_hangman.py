# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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
    lines = inFile.readlines()
    print(lines)
    # for item in lines:
    #     item = item.rstrip()
    # print(lines)
    # wordlist: list of strings
    # wordlist = lines.split('\n')
    # print(wordlist)

    print("  ", len(lines), "words loaded.")
    return lines

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
chosen = choose_word(wordlist)
print(chosen)
# your code begins here!
