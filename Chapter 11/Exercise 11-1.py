"""Write a function that reads the words in words.txt and stores
then as keys in a dictionary. It doesn't matter what the values
are. Then you can use the in operator as a fast way to check whether
a string is in the dictionary.

If you did Ex. 10-10, you can compare the speed of this
implementation with the list in operator and bisection search"""


def appen():
    words = []
    fin = open('words.txt')
    for line in fin:
        stripped = line.strip()
        words.append(stripped)
    return words


def dict(words):
    dict = {}
    fin = open('words.txt')
    for line in fin:
        dict[line] = 1
    print(dict)

dict(appen())
