
# Response 0
# The postcondition verifies that return_value matches the n-th term of the Fib4 sequence by using functools.reduce to iteratively compute the sum of the four preceding terms, starting from the initial sequence values for n=0, 1, 2, and 3.
assert return_value == ((0, 0, 2, 0)[n] if n < 4 else __import__('functools').reduce(lambda s, _: (s[1], s[2], s[3], sum(s)), range(4, n + 1), (0, 0, 2, 0))[-1])


