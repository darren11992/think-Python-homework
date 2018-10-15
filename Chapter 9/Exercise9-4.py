"""Write a funtion named uses_only taht takes a word and a string of
letters, and that returns True if the word contains only the letters
in the list. Can you make a sentence using only the letters
"acefhlo"? (other than "Hoe alfalfa"?)"""


def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True

# To answer question:


def uses_only_test(letters):
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if uses_only(word, letters):
            print(line)


#uses_only_test("acefhlo")
print(uses_only("abstemious", "aeiou" ))