"""Write a function called cumsum that takes a list of numbers and 
returns the cumulative sum; that is, a new list where the ith 
element is the sum of the first i+1 elements from the original list
For example:

>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]"""


def cumsum(no_list):
    cumsum = []
    for i in range(len(no_list)):
        if i == 0:
            cumsum.append(no_list[i])    
        else:
            cumsum.append(no_list[i]+no_list[i-1])
    return cumsum

print(cumsum([1, 2, 3]))
