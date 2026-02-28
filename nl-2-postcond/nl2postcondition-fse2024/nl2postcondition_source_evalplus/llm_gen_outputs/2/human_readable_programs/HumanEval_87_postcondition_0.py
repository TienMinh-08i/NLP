# The return_value must be the list of all (row, col) coordinates where lst[row][col] == x, sorted primarily by row ascending and secondarily by column descending.
assert return_value == sorted([(r, c) for r, row in enumerate(lst) for c, val in enumerate(row) if val == x], key=lambda p: (p[0], -p[1]))


