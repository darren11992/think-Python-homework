"""Write a program that reads text.txt and prints only the words with
more than 20 characters (not counting whitespace)"""


fin = open('words.txt')
# Open takes returns a file object that can be used to read the file.
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)
