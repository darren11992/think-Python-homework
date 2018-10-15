"""Two words are anagrams if you can rearrange the letters from one
to spell the other. Write a function called is_anagram that takes
two strings and returns True if they are anagrams"""

def is_anagram(string1, string2):
    list1 = list(string1)
    list2 = list(string2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

print(is_anagram("anna", "naa"))
