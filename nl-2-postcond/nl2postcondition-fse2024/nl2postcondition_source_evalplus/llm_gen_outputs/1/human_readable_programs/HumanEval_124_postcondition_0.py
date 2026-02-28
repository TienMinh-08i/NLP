# The postcondition asserts that the `return_value` is True if and only if the input `date` string
# satisfies all validation rules: it must be 10 characters long, have hyphens at positions 2 and 5,
# its month (first two characters), day (characters 3-4), and year (characters 6-9) parts must all
# consist of digits. Furthermore, after converting the month and day parts to integers, the month
# must be between 1 and 12 (inclusive), and the day must be between 1 and the maximum allowed days
# for that specific month, where February is considered to have 29 days.
days_in_month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
assert return_value == (
    len(date) == 10 and
    date[2] == '-' and
    date[5] == '-' and
    date[:2].isdigit() and
    date[3:5].isdigit() and
    date[6:].isdigit() and
    (lambda m_val, d_val:
        1 <= m_val <= 12 and
        1 <= d_val <= days_in_month_list[m_val - 1]
    )(int(date[:2]), int(date[3:5]))
)


