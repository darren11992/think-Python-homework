"""Write a function called most_frequent that takes a string and
prints the letters in decreasing order fo frequency. Find text
samples from several different languages and see how letter
frequency varies between languages. Compare your results with
the tables at http://en.wikipedia.org/wiki/Letter_frequencies """

"""
def histogram(string):
    d = {}
    for char in string:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d


def most_frequent(string):
    histo = histogram(string)
    histoTuple = histo.items()
    print(histoTuple)
    print(histoTuple[1])

most_frequent("Potato")
"""

def most_frequent(string):
    d = {}
    for char in string:
        if char not in string