"""
- Strings are sequences of characters.

- The bracket operator allows you to select individual characters
  in a string:
  eg:
  	fruit = 'banana'
  	letter = fruit[2] --> 'n' 
  	Note: string indexs begin at 0.

-The len() function returns the length of a string. The final index
 of a string is always its length -1.

- A traversal is going over each character in a loop iteratively,
  usually done with a while loop.

- The bracket operator also allow you to 'splice' strings;
  Eg:
  	fruit[:3]---> 'ban'
  	fruit[3:]---> 'ana'
  	In general: string[n:m]--> produce a string from the nth to the 
  	character before the mth term.

- Strings are immutable, meaning an existing string cannot be changed.
  Eg:
  	string = "Hello, World"
  	string[0] = 'h' ---> will produce a TypeError.
  	The best you can do is create a new string thats a varient.
  	new_string = 'J' + string[1:]
  	print(new_string)----> 'Jello, World'

- Strings have several methods like .upper() or .find(). They use dot	
  notation, with the strings name going behind the dot.
  Eg:
  	fruit.upper()----> 'BANANA'
  	fruit.find('a')---- returns '1' (index of first 'a') 

- The in operator returns a boolean value if the string to the left
  of it is a substring of the one to its right.
  Eg:
  	'a' in 'banana'---> True
  	'c' in 'banana' --> False
"""
