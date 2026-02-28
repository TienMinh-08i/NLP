# The postcondition asserts that the function's return value ('Yes' or 'No') correctly reflects whether the input file_name meets all specified validity criteria:
# 1. The file name contains no more than three digits.
# 2. The file name contains exactly one dot.
# 3. The substring before the dot is not empty and starts with a letter from the Latin alphabet.
# 4. The substring after the dot is one of 'txt', 'exe', or 'dll'.
assert (
    (
        len(list(filter(lambda ch: ch.isdigit(), file_name))) <= 3
        and len(file_name.split('.')) == 2
        and len(file_name.split('.')[0]) > 0
        and file_name.split('.')[0][0].isalpha()
        and file_name.split('.')[1] in ["txt", "exe", "dll"]
    ) == (return_value == 'Yes')
)


