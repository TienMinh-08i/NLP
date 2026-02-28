# The postcondition verifies that the function returns True if the list q is a palindrome and the sum of its elements is less than or equal to w, and False otherwise.
assert return_value == (q == q[::-1] and sum(q) <= w)


