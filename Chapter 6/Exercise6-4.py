"""A number, a, is a power if b if it is divisible by b and a/b is a power of b. 
Write a function called is_power that takes parameters a and b and returns True if a is a power 
of b. Note: you will have to think about the base case."""

def is_power(a, b):
	if a == 1 and b == 1:
		return True					#My attempt.
	else:
		if a % b == 0:
			return is_power(a/b, b)


def is_power_correct(a,b):
	if a % b == 0:
		if a == b: # difficult base case tbh, was very nearly there.
			return True
		else:
			return is_power_correct(a/b, b)
	else:
		return False