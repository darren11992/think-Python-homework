"""The mathematican Srinivase Ramanujan found an infinite series
that can be used to generate a numerical approximation of 1/π:

'dench formula shown'

Write a function called estimate_pi that uses this formula to compute
and return an estimate of π. It should use a while loop to compute
terms of the summation until the last term is smaller that 1e-15.
You can check the last result by comparing it to math.pi
"""

import math


def estimate_pi():
    k = 0
    added = 0
    while added < 1e-30:
        total = 0
        added = ((math.factorial(4*k)*(1103+(26390 * k)))
                 / ((math.factorial(k)**4) * (396**(4*k))))
        total += added
        k += 1
    estimate = (2 * math.sqrt(2) / 9801) * total
    print("The estimate for 1/π is:", estimate)
    print("Python's value is:      ", (1/math.pi))


estimate_pi()
