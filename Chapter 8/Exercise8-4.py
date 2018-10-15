"""The following functions are all intended to check whether a 
string contains any lower-case letters, but at least some of them
are wrong. For each function, describe what the function actually
does (assuming the parameter is a string)"""


def any_lowercase1(s):
    for c in s:
        print(c)
        if c.islower():
            return True
        else:
            return False


"""This function correctly set up to iterate through each 
character however, due to the returns, on either path of the is/else
the function will not continue to execute after the first character
has been checked, as one of the returns will pull the program out 
of the function."""


def any_lowercase2(s): 
    for c in s:
        if 'c'.islower():
            return True
        else:
            return False


"""This function incorrectly checks the character 'c' due to the ''
either side of it, rather than the corrospondng variable which
would be checked if the '' were not there."""

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

"""This function iterates through each character and updates the flag
variable depending if the currect letters case. However, due to 
the flag updates, the final return value is only dependent on the 
final characters case. Eg: "bananA" --> False."""

def any_lowercase4(s):
    flag = False
    for c in s:
        if not c.islower():
            return False
    return True
"""This function iterates through each charcter and as soon as it
hits an Upper case one, returns False. If it gets through the string 
without an upper case letter, True is returned. A major issue here
is that the flag variable is assigned, but never used."""


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


"""Same as example four, without the unnessesary flag variable"""