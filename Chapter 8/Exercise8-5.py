"""A Caesar cypher is a weak form of encryption that involves
"rotating" each letter by a fixed number of places. To rotate a
letter means to shift through the alphabet, wraping around to the
beginning if necessary, so "A" rotated by 3 is "D" and "Z rotated
by 1 is A"

To rotate a word, rotate each letter by the same amount. For example
"cheer" rotated by 7 is "jolly" and "melon" rotated -10 is "cubed".

Write a function called rotate_word that takes a string and
integer as parameters, and returns a new string that contains the
letters from the original string rotated by the given amount.

You might want to use the built-in function ord, which converts a
character to a numeric code and chr, which does the opposite. Eg:

ord('c') - ord('a') = 2. Because c is the two-eth letter of the
alphabet. Beware though, upper case characters have different codes.
"""


def rotate_word(string, turns):
    new_string = ''
    for letter in string:
        char_code = ord(letter)
        if char_code > 122 and letter.islower(): # Incase the code goes above z's
            char_code -= 26
        elif char_code > 90 and not letter.islower():
            char_code -= 26
        elif char_code <97 and letter.islower():
            char_code += 26
        elif char_code <65 and not letter.islower():
            char_code += 26
        new_char = chr(char_code + turns)
        new_string += new_char
    print(new_string)

rotate_word("melon", -10)

