"""Write a function called has_duplicates that takes a list and
returns True of there is any element that appears more than once.
It should not modify the original list"""


def has_dupicates(t):  # t is a list
    t1 = t[:]  # Prevents main list being effected
    t1.sort()
    for i in range(len(t1)):
        if i != len(t1)-1:
            if t1[i] == t1[i + 1]:
                return True
    return False


"""The following from stack overflow is also quite neat.
   It only works for lists contain hashable elements
   (numbers and strings, not list and dictionaries)"""


def has_dupicates2(t):
    t1 = t[:]
    if len(t1) != len(set(t1)):
        """Sets must have unique elements. If elements are removed, there
        must be duplicates in the list"""
        return True
    else:
        return False


print(has_dupicates([1, 2, 3, 4]))      # False
print(has_dupicates2([1, 2, 3, 4]))     # False
print(has_dupicates([1, 1, 2, 3, 4]))   # True
print(has_dupicates2([1, 1, 2, 3, 4]))  # True
