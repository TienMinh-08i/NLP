```python
# The postcondition checks that if the input string is empty, the output is also empty.
# Otherwise, it ensures that the output string contains the same number words as the input,
# but sorted numerically from smallest to largest, and that all words in the output are valid number words.
assert (numbers == "" and return_value == "") or \
       ((lambda to_int_map:
            (lambda input_words_list, output_words_list:
                sorted(input_words_list) == sorted(output_words_list) and # Checks content preservation and same number of words
                all(w in to_int_map for w in output_words_list) and       # Ensures all output words are valid number words
                (len(output_words_list) <= 1 or # For lists with 0 or 1 element, they are considered sorted
                 all(to_int_map[output_words_list[i]] <= to_int_map[output_words_list[i+1]]
                     for i in range(len(output_words_list) - 1)))
            )(numbers.split(" "), return_value.split(" "))
        )({'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}))
```


