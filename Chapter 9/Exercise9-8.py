"""Heres another car talk puzzler (http://www.cartalk.com/content/puzzlers):
"I was driving down the highway the other day and I happened to notice
my odometer. Like most odometers, it shows six digits, in whole miles
only. So, if my car had 300,000 miles for example, id see
3-0-0-0-0-0. Now, what I saw that day was interesting. I noticed the
last four digits were palindromic; that is, they read the same forwards
as backwards. For example, 5-4-4-5 is a palindrome, so my odometer
read 3-1-5-4-4-5.

One mile later, the last five numbers were palindromic. For example,
it might have read 3-6-5-4-5-6. One mile after that, the middle 4
out of the six digits were palindromic. Then the next mile, all six
were palindromic!!!

The question: what was on the odometer, when I first looked?

Write a python program that tests all the six-digit numbers and prints
any numbers that satisfy these requirements"""


def odometer():
    all_nos = []
    meter = 100000
    while meter < 999999:
        original_meter = meter
        if is_palindrome(last_n_digits(meter, 4)):
            meter += 1
            if is_palindrome(last_n_digits(meter, 5)):
                meter += 1
                if is_palindrome(meter, 2):
                    meter += 1
                    if is_palindrome(meter):
                        all_nos.append(original_meter)
        meter += 1
    return all_nos


def is_palindrome(number, indent=0):
    # indent = how many characters into the number is the palindrome.
    string_no = str(number)
    indented_string = string_no[indent: len(string_no)-indent]
    if indented_string[0:] == indented_string[::-1]:
        return True
    else:
        return False


def last_n_digits(number, n):
    """Grabs the lasts n digits of a number, regardless of its size."""
    number = str(number)
    return number[len(number)-n:]


print(odometer())
# The number is 198888 or 199999!
