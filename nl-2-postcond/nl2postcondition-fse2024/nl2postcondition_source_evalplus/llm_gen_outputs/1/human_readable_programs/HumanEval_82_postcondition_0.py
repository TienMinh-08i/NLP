# The postcondition asserts that the returned value is True if the length of the input string is a prime number, and False otherwise.
assert return_value == (len(string) > 1 and all(len(string) % i != 0 for i in range(2, int(len(string)**0.5) + 1)))


