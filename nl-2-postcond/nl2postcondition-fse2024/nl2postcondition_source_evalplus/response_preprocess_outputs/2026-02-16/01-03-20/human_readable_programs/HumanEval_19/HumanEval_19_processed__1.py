from typing import List

def sort_numbers_original(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    to_int = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    if numbers == '':
        return ''
    return ' '.join(sorted(numbers.split(' '), key=lambda n: to_int[n]))


def sort_numbers(numbers: str) -> str:


    return_value = sort_numbers_original(numbers)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition asserts two main properties of the sort_numbers function's output:
    # 1. The returned string contains the same number words as the input string, just potentially reordered.
    # 2. The number words in the returned string are sorted from smallest to largest according to their numerical value.
    # It also handles the edge case where the input string is empty.
    to_int = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    assert (
        (numbers == "" and return_value == "") or
        (
            numbers != "" and
            # Check that the return value contains the same elements as the input, maintaining counts.
            sorted(numbers.split(" ")) == sorted(return_value.split(" ")) and
            # Check that the elements in the return value are sorted according to their numerical value.
            all(to_int[return_value.split(" ")[i]] <= to_int[return_value.split(" ")[i+1]]
                for i in range(len(return_value.split(" ")) - 1))
        )
    )
    

    return return_value
