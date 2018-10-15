"""Write a function named avoids that takes a word and a string of
forbidden letters and returns True if the word doesn't use any of the
forbidden letters. Modify the program to prompt the user to enter a
string of forbidden letters and then print the number of words that
don't contain any of them. Can you find a combination of five
forbidden letters that excludes the smallest number of words?"""


def avoids(word, letters):
    # letters are characters that are to be avoided
    for letter in letters:
        if letter in word:
            return False
    return True


def avoided_words():
    fin = open('words.txt')
    forbidden_input = input("Enter the letters you want to be forbidden:")
    forbidden_letters = forbidden_input.replace(" ", "")
    total = 0
    for line in fin:
        if avoids(line, forbidden_letters):
            total += 1
    print(total)


avoided_words()
