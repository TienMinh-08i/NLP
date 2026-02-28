
# Response 0
# The postcondition verifies that return_value matches the English names of integers from arr that are between 1 and 9 inclusive, sorted in descending order.
assert return_value == list(map(lambda x: {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}[x], sorted(filter(lambda y: 1 <= y <= 9, arr), reverse=True)))


