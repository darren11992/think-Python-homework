"""Copy the loop from "Square roots" on page 79 and encapsulate it
in a function called mysqrt that takes a as a parameter, chooses
a reasonable value of x, and returns an estimate of the square root
of a. To test it, write a function named "test_square_root that
prints a table like this:
First column: a number, a.
Second column: a's square root, computed with my_sqrt.
Third column: a's square root, computed with math.sqrt.
Fourth column: the difference between the two square roots.
"""
import math


def mysqrt(a):
    x = a - .05
    while True:
        y = (x + a/x) / 2
        #print(abs(y-x))
        if abs(y-x)< 0.0000001:
            break
        x = y
    return y


def test_square_root():
    print("a    mysqrt(a)    math.sqrt()    diff")
    print("-    ---------    -----------    ----")
    a = 1
    while a < 10:
        print(a, mysqrt(a),math.sqrt(a),
              max(mysqrt(a), math.sqrt(a)) - min(mysqrt(a), math.sqrt(a)))
        a += 1

#Note: This produces a shit table.
test_square_root()
