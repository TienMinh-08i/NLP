```python
import re

# Helper function to convert a mini roman numeral string to an integer.
# This function is designed to be purely functional, using recursion.
# It handles the specific mini-roman rules (lowercase, values up to 1000).
def _mini_roman_to_int(s):
    # Mapping of Roman numeral characters to their integer values.
    roman_map = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}

    # Recursive helper to process the string.
    def _parse_recursive(current_string, current_sum):
        # Base case: if the string is empty, return the accumulated sum.
        if not current_string:
            return current_sum

        # Get the value of the first character.
        first_char = current_string[0]
        # Use .get with a default of 0 for robustness, although regex should prevent invalid chars.
        first_char_val = roman_map.get(first_char, 0)

        # Check for subtractive cases (e.g., 'iv' for 4, 'ix' for 9, etc.)
        if len(current_string) > 1:
            second_char = current_string[1]
            second_char_val = roman_map.get(second_char, 0)
            if first_char_val < second_char_val:
                # If a smaller value precedes a larger value, it's a subtraction.
                # Process the rest of the string after these two characters,
                # adding the difference to the sum.
                return _parse_recursive(current_string[2:], current_sum + (second_char_val - first_char_val))

        # Additive case: simply add the current character's value.
        # Process the rest of the string after the first character.
        return _parse_recursive(current_string[1:], current_sum + first_char_val)

    # Start the recursive parsing with the full string and an initial sum of 0.
    return _parse_recursive(s, 0)

# The postcondition asserts that the return_value is a string, composed only of valid lowercase Roman numeral characters,
# is entirely in lowercase, and when converted back to an integer, it matches the original input number.
assert (isinstance(return_value, str) and \
        re.fullmatch(r"^[ivxlcdm]*$", return_value) is not None and \
        return_value == return_value.lower() and \
        _mini_roman_to_int(return_value) == number)
```


