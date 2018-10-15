"""Two words are "rotate pairs" if you can rotate one of
them and get the other (see rotate_word in Ex 8-5). 

Write a program that reads a wordlist and finds all the 
rotate pairs """

#From 8-5 (improved haha):


def rotate_word(string, turns):
    new_string = ''
    for letter in string:
        char_code = ord(letter)
        new_char = char_code + turns
        if new_char > 122 and letter.islower(): # Incase the code goes above z's
            new_char -= 26
        elif new_char > 90 and not letter.islower():
            new_char -= 26
        elif new_char < 97 and letter.islower():
            new_char += 26
        elif new_char < 65 and not letter.islower():
            new_char += 26

        new_string += chr(new_char)
    return new_string


def make_word_list():
    word_list = []
    fin = open("words.txt")
    for word in fin:
        word_list.append(str(word))
    return word_list


def rotation_check(turns):
    word_list = list(make_word_list())
    d = {}
    matches = {}
    for word in word_list:
        rotated_word = rotate_word(word, turns)
        #print(rotated_word)
        if rotated_word in d:
            print(word, rotated_word) #This is bs. Store all words in a dic and check it.
            matches[word] = rotate_word
            word_list.remove(rotate_word)
        d[rotate_word] = "checked"
    if len(matches) == 0:
        return None
    else:
        return matches

print(rotation_check(-10))
