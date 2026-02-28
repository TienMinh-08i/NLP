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
    
    # This postcondition asserts two main properties:
    # 1. The returned string is a permutation of the input string's number words, meaning it contains the exact same words with the same frequencies.
    # 2. The number words in the returned string are sorted in ascending order based on their numerical values.
    assert (
        # Define the mapping from number word to integer value within the expression's scope
        (lambda to_int_map:
            # Define the input and output lists of words, handling empty strings gracefully
            (lambda input_words, output_words:
                # Property 1: Check if the output is a permutation of the input words
                # This is done by sorting both lists and comparing them.
                sorted(input_words) == sorted(output_words) and
                # Property 2: Check if the output words are sorted numerically
                # This is done by iterating through adjacent pairs and comparing their integer values.
                all(to_int_map[output_words[i]] <= to_int_map[output_words[i+1]]
                    for i in range(len(output_words) - 1))
            )(
                # Arguments for the inner lambda: input_words and output_words
                numbers.split(" ") if numbers else [],  # Handle empty input string
                return_value.split(" ") if return_value else [] # Handle empty return value string
            )
        )(
            # Argument for the outer lambda: the to_int_map dictionary
            {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
        )
    )
    

    return return_value
