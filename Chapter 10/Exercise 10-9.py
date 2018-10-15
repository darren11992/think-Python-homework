"""Write a function that reads the file words.txt and builds a list
with one element for each word. Write two versions, one with append,
one using t = t + [x]. Which is quicker and why?"""


def append():
    words = []
    fin = open('words.txt')
    for line in fin:
        stripped = line.strip()
        words.append(stripped)
    print("done append")
    # This bangs threw it.


def idium():
    words = []
    fin = open('words.txt')
    for line in fin:
        stripped = line.strip()
        words = words + [stripped]
    print("done idium")
    # This is pathetically slow.


idium()
append()
