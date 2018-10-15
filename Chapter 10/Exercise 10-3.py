"""Write a function called middle that takes a list and returns a 
new list that contains all but the first and last elements.
For example:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    >>> [2, 3]"""

def middle(t):
    new_t = t[:] 
    # new_t = t will use the same reference for both lists
    del new_t[0]
    del new_t[len(new_t)-1]
    return new_t

print(middle([1, 2, 3, 4, 5, 6]))
