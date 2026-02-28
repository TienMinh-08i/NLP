# The postcondition verifies that the return_value is the middle element of the sorted list l if its length is odd, or the average of the two middle elements if its length is even.
assert return_value == (sorted(l)[len(l) // 2] if len(l) % 2 == 1 else (sorted(l)[len(l) // 2 - 1] + sorted(l)[len(l) // 2]) / 2)


