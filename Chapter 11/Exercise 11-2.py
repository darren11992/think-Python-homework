"""Read the docs for the dictionary method setdefault and use it 
to write a more consice version of invert_dict"""


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key] # Creates a new list
        else:
            inverse[val].append(key)


def invert_dict2(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse[val] = inverse.setdefault([key], inverse[val].append(key))


def hello():
    print("Hello")

hello()
