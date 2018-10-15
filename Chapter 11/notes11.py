"""
- A dictionary is similar to a list, but the indexs (keys), can be 
  defined, rather then just 0, 1, 2 etc.

- the function dict() creates dictionaries.

- Square brackets can be used to add stuff to dictioaries:
 Eg:
    >>> eng2spa = dict()
    >>> eng2spa['one'] = "uno"
    This adds the value uno to the dictionary, with its key being 
    'one'.
    
    >>> eng2spa
    {'one': 'uno'}

- In general, the order of dictionaries are unpredictable:
    >>> eng2spa = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
    >>> esp2spa
    {'one': 'uno', 'three': 'tres', , 'two': 'dos'}
    But the key-value pairs stay the same, so it doesn't really matter.

- If a key isn't in a dictionary an exception is raised
- len() returns the no. of key-value pairs
- The in operator works for keys, not values;
    Eg:
        >>> 'one' in eng2spa
        True
        >>> 'uno' in eng2spa
        False
    
    To see if a value is in a dictionary, use values() which returns
    a collection of values:

        >>> vals = eng2spa.values()
        >>> 'uno' in vals
        True

    Note: for dictionaries, in takes the same amount of time to find 
    something, regardless of the dicts length.

- Dictionaries can often be used as a counter collection:
Eg:
"""
def histogram(string):
    d = dict()
    for char in string:
        if char not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
"""
>>> h = histogram('potato')
>>> h
{'a': 1, 'o': 2, 'p': 1, 't': 2}


- A method called get can grab values when given the corrosponding key
  If the key isn't in the dictionary, it returns the default value,
  which is its second parameter:

  Eg: >>> h.get('a', 'poo')
      1
      >>> h.grt('d', 'poo')
      'poo'

- When you traverse a dict with a for loop, it goes through the dicts
  keys.

- While its fairly easy to find a value when you know the dictionary
  and key, its harder to find the key from its value. There may be 
  multiple values that have the same key and stuff. Heres an example 
  of how to find a key (k), from a value (v) in a certain dict (d):
"""

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
        else:
            raise LookupError()
"""
note: the raise statement just causes a normal, customised exception.
You still get a normal traceback and error message.

- A list can be a values within a dictionary too. This example,
produces an inverted output to the string character count above:
"""
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse
            inverse[val] = [key] # Creates a new list
        else:
            inverse[val].append(key) # Adds the characer to an existing list
"""
>>> h = histogram('potato')
>>> h
{'a': 1, 'o': 2, 'p': 1, 't': 2}
>>> invert_dict(h)
{1: ['a', 'p'], 2: ['o', 't']}

- Lists cannot be keys in a dictionary because keys must be hashable
and lists are not. (hash = takes a value, returns an int) Due to lists
mutable nature, its too easy to create multiple keys refering to the 
same value if the list is changed.

- A previously computed value that is stored for later is called a
memo.

- variables defined in __main__ are global. They can be refered to in
any function and are often used as flags (boolean values that indicate
if a condition is true) They can be difficult though:
    Eg:
        been_called = False

        def example2():
            been_called = True

        When ran been_called doesnt change. The function creates a
        local variable of the same name, which expires at the
        when the function is done, and has no effect on the global.
        Global variables have to be defined properly before they can 
        be used within functions:

        been_called = False

        def example2():
            global been_called
            been_called = True

        If the global is mutable (ie. a dict) then this defining
        isnt required.
        Globals can be useful, but having lots creates a hard to
        debug value. 

- Dictionaries can make recursive functions far more efficient by 
  using them to store every value that is calculated of an arguement
  for a function. For example, once fib(4) is known as a value,
  it can be found in the dictionary and doesnt need to be calculated
  again.
        