"""Write a function called is_abecedarian that returns true if the
letters in the a word appear in alphabetical order (double letters
are okay). How many abercadarian words are there?"""


def is_abecedarian(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word_list = list(word)
    i = 0
    for letter in word_list:
        if i == len(word_list)-1:
            break
        elif alphabet.find(word_list[i]) > alphabet.find(word_list[i+1]):
            """If the left value is greater than the right, it comes later
            in alphabet, so the letters dont come in the correct order"""
            return False
        i += 1
    return True


def is_abercedarian_test():
    fin = open('words.txt')
    total = 0
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            total += 1
    print(total)


is_abercedarian_test()
# 596 words total.