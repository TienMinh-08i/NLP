# The postcondition checks that the return_value is True if and only if there exists an integer i in the range [-abs(a), abs(a)] such that i cubed is equal to the input integer a.
assert return_value == any(i**3 == a for i in range(-abs(a), abs(a) + 1))


