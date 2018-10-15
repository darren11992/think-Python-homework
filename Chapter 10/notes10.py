"""Chapter 10: Lists.

WHATS A LIST
-A list is a sequence of values and they can be any type.

HOW DO I MAKE ONE?
- They care created with square brackets
	Eg:
		numbers = [1, 2, 3, 4]
		veg = ['potato', ' carrot', 'broccoli']
	As above, these lists can be assigned to variables.

ARE THEY MUTABLE?
- Lists are mutable, so they can be modified after being created.
  The bracket operator is also used to access individual elements
  in a list:
  	Eg:
  		>>> numbers = [2, 5]
  		>>> number[1] = 123
  		>>> numbers
  		[2, 123]

THE IN OPERATOR AND LISTS
- The in operator also works the same way with lists:
	Eg:
		>>> 2 in numbers
		True
		>>> 'potato' in numbers
		False

TRAVERING LISTS
- A for loop can be used to traverse a list. However, using range and
  len also allows you access to the indexs of the elements;
	Eg:
		for i in range(len(numbers)):
			number[i] = number[i] * 2
	Len gets the no. of elements and range produces a list from 0 to 
	n-1.

NESTING
- If a list is within a list, it is nested. The nested list is still
  a single element in the parent list, regardless of the nested list
  size.

LIST OPERATIONS
- The two main operations that can be used on lists are + and *.
  + concatemates a list:
	Eg:
		>>> a = [2, 4, 6]
		>>> b = [1, 3, 5]
		>>> c = a + b
		>>> c
		[2, 4, 6, 1, 3, 5]
  
  * repeats the list:
    Eg:
    	>>> [0] * 4
    	[0, 0, 0, 0]
    	>>> [1, 2, 3] * 3
    	[1, 2, 3, 1, 2, 3, 1, 2, 3]

SLICING LISTS
- Lists can be sliced in the same way as stings. Its a good idea to 
  make a copy of the original list.

LIST METHODS
- There are tons of lists methods that do several different things.
  Most return None, so the syntax of using them is usually to just 
  write them, rather then use them to assign values to variables.
  Eg:

  >>> a = [1,2,3]
  >>> a = a.append(4)   # Incorrect
  >>> a
  None   

  >>> a = [1, 2, 3]
  >>> a.append(4)      # Correct
  >>> a
  [1, 2, 3, 4]

  Heres a few thats in the book:
  1: list.Append(element) - Adds element to list.
  2: list1.extent(list2) - Adds list 2 onto the end of list 1.
	List 2 is left unmodified.
  3: list.sort() - arranges elements from low to high.

REDUCE, MAPS AND FILTERS
- To get the sum of the elements in a list, use sum(list):
 Eg:
 	>>> a =[1, 2, 3]
 	>>>sum(a)
 	6
 The use of combining elements in into a singular value is called
 reduce.


- If you traverse a list and create a second, converting each element
 into something else, this ais called a "map" (map each previous 
 element to a new one)
  Eg:
  	
  	def capitalise(list):
  		capitals = []
  		for letter in list:
  			capitals.append(letter)
  		return capitals

- If you traverse a list, but only take certain elements for the second
  list, this is called a filter.
  Eg:
  	def only_upper(list):
  		uppers = []
  		for letter in list:
  			if letter.isupper():
  				uppers.append(letter)
  		return uppers

- Most list operations are a combinations of reduce, maps, and filters.

REMOVING SHIT FROM LISTS
- There are also several ways to remove elements form lists. Here a 
  few:

  1: list.pop(element's index) removes element from list and
     also returns it.
   Eg:
		>>> t = ['a', 'b', 'c']
		>>> x = t.pop(1)
		>>> t
		['a', 'c']
		>>> x
		'b'
  2: list.remove(element) uses the actual element (rather than its
     index) to remove it from the list. It returns nothing.

  3: del list[slice] uses a slice to remove element(s). Good if you
     have multiple elements to cull.

LISTS TO STRINGS AND BACK AGAIN
- There are several functions/methods that break a string up to a list:
  1: list(string): breaks string into a list of characters.
  2: string.split(delimiter) breaks a multi worded string into a list 
  of the words if the arguement is empty. If theres a delimeter it
  splits it based on that:
  	Eg:
  		>>>date = "2-5-75"
  		>>>d_m_y = date.split('-')
  		>>>d_m_y
  		['2', '5', '75']

  Note that split returns the list. It does not replace the string 
  with the list.

- join is the opposite of split. It takes a list and forms a single
  string from it. Join again returns the string, allowing variable
  assignment.

ALLISING AND LISTS
- the is operator allows you to see f multiple variables refer to the
  same value.
  	Eg:
  		>>> a = 'banana'
  		>>> b = 'banana'
  		>>> a is b
  		True

  Its important to note that when you create multiple identical lists,
  they do not refer to the same list:
    Eg:
    	>>> a = [1, 2, 3]
    	>>> b = [1, 2, 3]
    	>>> a is b
    	False
    The lists are equivelent, but not identical.

- You can assign objects to variables and they will be identical.
	Eg:
		>>> a [1, 2, 3]
		>>> a = b
		>>> b is a 
		True
	The object now has two references (assosiations with variables)
	Now, when one is manipulated, so is the other (since lists are
	mutible):
	    >>> b[0] = 22
	    >>> a
	    [22, 2, 3]
	This is cool, but also error prone and should be avoided where
	possible. For immutable objects (ie. strings) allising is rarely
	an issue.

- Unlike a string, when a list is passed to a function, the function
  uses its original reference, even if its refered to with a different
  name within the function. An alternative is to create and return a 
  new list within a function.

- Remember that some list operations modify lists and some create new 
  ones. 
