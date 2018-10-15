"""Write a program that reads a file, breaks each line into words,
strips whitespace and punctuation from the words, and converts them
to lowercase. """

import string

def stripFile(file):
    fin = open(file)
    for line in fin:
        word = ''
        for letter in line:
            if letter in string.whitespace:
                # Stick the now made work in a data structure
                # Make sure the loop contines building the next word.
                # Then make sure punctuation works.
            else:
                word += letter
            print(word)

stripFile('test.txt')