"""This exercise pertains to the so-called Birthday Paradox, which
you can read about here: http://en.wikipedia/wiki/Birthday_paradox.

If there are 23 students in your class, what are the chances that two
of you have the same birthday? You can estimate this probability by
generating random samples of 23 birthdays and checking the matches.

Hint: you can generate random birthdays with the randint function in
the random module.

The authors solution is here: http://thinkpython2.com/code/birthday.py
"""


from random import randint, choice


def has_duplicates(t):
    t1 = t[:]
    if len(t1) != len(set(t1)):
        return True
    else:
        return False


def has_duplicates2(t):  # t is a list
    t1 = t[:]  # Prevents main list being effected
    t1.sort()
    for i in range(len(t1)):
        if i != len(t1)-1:
            if t1[i] == t1[i + 1]:
                return True
    return False


def has_duplicates3(t):
    if any(t.count(x) > 1 for x in t):
        """list.count(x) records the amount of times x is in list.
        for x in t iterates through the list. Stack Overflow gave
        me this"""
        return True
    else:
        return False


def produce_birthday():
    day = randint(1, 31)
    if day == 31:
        month = choice([1, 3, 5, 7, 8, 10, 12])
    else:
        month = randint(1, 12)
    birthday = [day, month]
    return birthday


def produce_birthday_list(size):
    birthdays = []
    for i in range(size + 1):
        birthdays.append(produce_birthday())
    return birthdays


def main(tests, class_size):
    duplicates = 0
    for i in range(tests + 1):
        birthdays = produce_birthday_list(class_size)
        if has_duplicates3(birthdays):
            duplicates += 1
    probability = duplicates / tests
    return probability


print(main(100000, 70))  # 0.99922
print(main(100000, 23))  # 0.54079
