# The total number of bucket lowerings should be the sum of the ceiling of (water in each well / bucket capacity).
assert sum(map(lambda well: (sum(well) + capacity - 1) // capacity, grid)) == return_value


