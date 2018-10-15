"""In 1939 Ernest Vincent Wright published a 50,000 word novel called
Gadsby that does not contain the letter "e". Since "e" is the most
common letter in English, that's not easy to do.

In Fact, it is difficult to construct a solitary thought without using
that most common symbol. It is slow going at first, but with caution
and hours of training, you can gradually gain facility.

haha

Write a function called has_no_e that returns True of the given word
doesn't have "e" in it.

Modify the program from 9-1, to print only words that have no "e",
and compute the percentage of words in the list that have no "e".
"""


def no_e(word):
    if "e" not in word:
        return True
    else:
        return False

# from 9-1:


fin = open('words.txt')
# Open takes returns a file object that can be used to read the file.
count = 0
no_e_list = []
for line in fin:
    count += 1
    word = line.strip()
    if no_e(word):
        no_e_list.append(word)
percentage = (len(no_e_list)/count) * 100
print(percentage)
