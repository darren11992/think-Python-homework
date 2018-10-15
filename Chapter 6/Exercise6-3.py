"""
A palindrome is a word that is spelled backward
and forward, like "noon" and "redivider". Recursively,
a word is a palindrome if the first and last letters
are the same and the middle is a palindrome.

The following are functions that take a string arguement and return
the first, last and middle letters:

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

1: Write a function called is_palindrome that takes a
string arguement and returns True if it is a palindrome
and False otherwise. Remember that you can use the
built in function lento check the length of a string.
"""


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) < 2 or word[0] != word[-1]:
        return False

    elif len(word) == (2, 3) or len(word) == 3 and word[0] == word[-1]: 
        return True
    
    elif len(word) > 2 and word[0] == word[-1]:
        return is_palindrome(word[1:-1])

# works
