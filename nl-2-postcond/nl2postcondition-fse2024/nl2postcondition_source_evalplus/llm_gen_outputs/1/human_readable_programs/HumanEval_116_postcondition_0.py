# This postcondition verifies two properties of the sort_array function's return value:
# 1. It is a permutation of the input array `arr`, meaning it contains the same elements with the same frequencies.
# 2. It is sorted according to the specified criteria: primarily by the count of '1's in the binary representation
#    (as defined by the function's internal `cmp` logic) in ascending order, and secondarily by the decimal value
#    in ascending order for elements with an equal count of '1's.
assert (len(return_value) == len(arr) and
        all(map(lambda x: return_value.count(x) == arr.count(x), set(arr))) and
        all(map(lambda i:
                (lambda ones_x, ones_y, x, y:
                    (ones_x < ones_y) or (ones_x == ones_y and x <= y)
                )(len(list(filter(lambda ch: ch == "1", bin(return_value[i])))),
                  len(list(filter(lambda ch: ch == "1", bin(return_value[i+1])))),
                  return_value[i],
                  return_value[i+1]),
                range(len(return_value) - 1))))


