"""Here's another car talk Puzzler you can solve with a search;

"Recently I had a visit with my mum and we realised that the two
digits that make up my age reversed resulted in her age. For 
example, if she's 73, I'm 37. We wondered how often this has 
happened over the years but we got sidetracted with other topics
and we never came up with the answer.

When I got home I figured out that the digits of our ages have been
reversible six times so far. I also figured out that if we're lucky
it would happen again in a few years, and if we're really lucky it
would happen one more time after that. In other words, it would happen
8 times overall. So the question is, how old am I now?"

Write a python program that searches fir solutions to this puzzler.
Hint: you might find the string method zfill useful"""


def is_opposite(first, second):
    """checks if a number reversed is the other number"""
    no1 = str(first)
    no2 = str(second)
    if no1[:] == no2[2::-1]:
        return True
    else:
        return False


def main():
    elder_ages = list(range(18, 100))
    younger_ages = list(range(0, 100))
    possible_ages = []
    for young_age in younger_ages:
        
        print(young_age, ":")
        for old_age in elder_ages:
            
            original_young_age = young_age
            original_old_age = old_age
            total = 0
            while old_age < 100:
                if is_opposite(old_age, young_age):
                    total += 1
                old_age += 1
                young_age += 1
            if total > 0:
                print(total, original_young_age, original_old_age)
            #if total == 8:
                #possible_ages.append(original_age)
    return possible_ages
    """possible_ages = []
    for age in elder_ages:
        younger_age = age - 18
        #if younger_age < 0:
            #pass
        #else:
        total = 0
        while age < 100:
            original_age = younger_age
            if is_opposite(age, younger_age):
                total += 1
            age += 1
            younger_age += 1
        if total == 8:
            possible_ages.append(original_age)
    return possible_ages
"""

print(main())


