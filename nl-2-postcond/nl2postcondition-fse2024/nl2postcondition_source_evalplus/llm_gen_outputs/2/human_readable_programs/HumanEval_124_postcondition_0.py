import re
# The postcondition verifies that return_value is True if and only if 'date' is a string in 'mm-dd-yyyy' format representing a valid date where the month is between 1 and 12, and the day is between 1 and the maximum allowed for that month (31 days for months 1, 3, 5, 7, 8, 10, 12; 30 days for months 4, 6, 9, 11; and 29 days for month 2).
assert return_value == (bool(re.match(r'^\d{2}-\d{2}-\d{4}$', date)) and 1 <= int(date[:2]) <= 12 and 1 <= int(date[3:5]) <= (31 if int(date[:2]) in [1, 3, 5, 7, 8, 10, 12] else 30 if int(date[:2]) in [4, 6, 9, 11] else 29))


