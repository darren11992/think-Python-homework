"""Write a function called is_sorted that takes a list as a parameter
and returns True if the list is sorted in ascending order and False
otherwise. For example:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted([b, a])
    False"""

def is_sorted(t):
    sorted_t = t[:]
    sorted_t.sort()
    if t == sorted_t:
        return True
    else:
        return False

print(is_sorted(['a', 'b' ,'c']))