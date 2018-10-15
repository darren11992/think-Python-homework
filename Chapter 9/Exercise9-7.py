"""This question is based on a puzzler that was broadcast on the radio
program Car Talk (http://www.cartalk.com/content/puzzlers):

Give me a word with three consecutive double letters. I'll give you
a couple of words that almost qualify, but don't. For example the 
word committee, c-o-m-m-i-t-t-e-e. It would be great except for the 
"i" that sneaks in there. Or mississippi: M-i-s-s-i-s-i-p-p-i. If you
take the "i"s it would work. But there is a word that has three
consequtive pairs of letter and to the best if my knowledge this
be the only word. Of course, there are probably 500 words but I can
only think of one. Whats the word?

Write a program to find out"""


def three_consecutive_test():
    fin = open('words.txt')
    all_words = []
    for line in fin:
        i = 0
        j = 1
        k = 2
        l = 3
        m = 4
        n = 5
        word = line.strip()
        while n < len(word):
            if (word[i] == word[j] and word[k] == word[l]
               and word[m] == word[n]):
                all_words.append(word)
            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
    return all_words


print(three_consecutive_test())  # Bookkeeper!!!

"""My way is correct, but this is the slightly more elegant solution
by the author:"""


def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.

    word: string

    returns: bool
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')
