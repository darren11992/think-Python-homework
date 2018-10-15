"""The built in function eval takes a string and evaluates it using
use python interpreter.
Write a function called eval_loop that iteratively prompts the user,
takes the resulting input and evaluates it using eval, and prints the
result.
It should continue until the user enters "done", and then, returns
the value of the last expression that was evaluated.
"""


def eval_loop():
    user_input = None
    while True:
        user_input = input("Type an expression to be evaluated:")
        if user_input == "Done":
            break
        else:
            print(eval(user_input))
    return user_input
# note: if a non-proposition is evaluated, an error occurs.


eval_loop()
