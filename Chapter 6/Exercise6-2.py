"""The Ackermann function, A(m,n), is defined:
      = n+1                 if m = 0
A(m,n)= A(m-1,1)            if m > 0 and n = 0
      = A(m-1, A(m, n-1))   if m > 0 and n > 0

Write a function named ack that evalulates the Ackermann function.
Use it to evaluate ack(3,4), which should be 125. What happens
for larger values of m and n?
"""


def ack(m, n):
    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return ack(m-1, 1)
    if m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))


""" At larger value the function actually fails,
    do to the recursion depth limit being met.
    This is a similar example to fibonaci, where
    when a function is recursed multiple times
    simultaniously, the runtime increases in an exponential."""
