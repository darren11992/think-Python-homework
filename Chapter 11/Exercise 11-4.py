"""If you did Exercise 10-7, you already have a function
called has_duplicates that takes a parameter and returns True
if htere is any object that appears more than once in the
list. Use a dictionary to write a faster, simpler version
of has_duplicates """

# Original:


def has_dupicates(t):  # t is a list
    t1 = t[:]  # Prevents main list being effected
    t1.sort()
    for i in range(len(t1)):
        if i != len(t1)-1:
            if t1[i] == t1[i + 1]:
                return True
    return False


def has_duplicates2(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = "in"
        print(d)
    return False


print(has_duplicates2([1, 2, 3, 4]))
print(has_duplicates2([1, 1, 2, 3, 4]))