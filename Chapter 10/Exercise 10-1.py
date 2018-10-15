"""Write a function called nested_sum that takes a list of lists of 
integers and adds up all the elements from all the nested lists"""


def nested_sum(numbers):
    total = 0
    for nest in numbers:
        total += sum(nest)
    return total

print(nested_sum([[1, 2], [3], [4, 5, 6]]))
