"""Two words are a "reverse pair" if each is the reverse of the
other. Write a program that finds all the reverse pairs in the word
list"""


def is_reverse_pair(word1, word2):
    reversed_2 = word2[::-1]
    if word1 == reversed_2:
        return True
    else:
        return False


def appen():
    words = []
    fin = open('words.txt')
    for line in fin:
        stripped = line.strip()
        words.append(stripped)
    return words


def in_bisect(list, key, i, j):
    if i >= j:
        if list[i] == key:
            return True
        else:
            return None
    else:                           # Binary Search
        mid = (i+j)//2
        if list[mid] == key:
            return True
        elif key < list[mid]:
            return in_bisect(list, key, i, mid - 1)
        else:
            return in_bisect(list, key, mid + 1, j)


def main():
    word_list = appen()
    pairs = 0
    for word in word_list:
        if in_bisect(word_list, word[::-1], 0, len(word_list) - 1):
            #print(word, "+", word[::-1])
            pairs += 1
    print("There are a total of", pairs, "pairs in the list")

print(main())
        
