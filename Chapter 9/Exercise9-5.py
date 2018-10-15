"""Write a function named uses_all that takes a word and
a string of required letters, and returns true if the word uses all
the required letters at least once. How many words are there that
use all the vowels aeiou? How about aeiouy"""


def uses_all(word, letters):
    """Function that returns true if the word given uses each letter
    in the string letters at least once"""
    required = word.strip()
    for letter in letters:
        if letter not in required:
            return False
    return True


def uses_all_test(letters):
    fin = open('words.txt')
    total = 0
    for line in fin:
        word = line.strip()
        if uses_all(word, letters):
            total += 1
    print(total)


uses_all_test("aeiouy")
