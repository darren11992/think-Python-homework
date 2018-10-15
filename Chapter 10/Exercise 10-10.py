"""To check whether a word is in the word list, you could use the in
operator, but it would be slow because it searches through the words
in order.

Because the words are in alphabetical order, we can speed things up
with a bisection search (aka. binary search).

A description of the binary search ensues.

Write a function called inbisect that takes a sorted list and a
target value and returns the index in the list if it's there and
None if its not."""


def in_bisect(list, key, i, j):
    if i >= j:
        if list[i] == key:
            return i
        else:
            return None
    else:                           # Binary Search
        mid = (i+j)//2
        if list[mid] == key:
            return mid
        elif key < list[mid]:
            return in_bisect(list, key, i, mid - 1)
        else:
            return in_bisect(list, key, mid + 1, j)


def appen():
    words = []
    fin = open('words.txt')
    for line in fin:
        stripped = line.strip()
        words.append(stripped)
    return words


def sort_words(t):
    t.sort()
    print
    return list


def main():
    first_list = appen()
    return in_bisect(first_list, 'hello', 0, len(first_list)-1)


print(main())
