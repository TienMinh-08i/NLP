
# Response 0
# The postcondition ensures that if the input string is empty or contains only spaces,
# the result is an empty dictionary. Otherwise, it verifies that the returned dictionary
# contains exactly those letters from the input that have the highest frequency,
# and that their associated counts are indeed that maximum frequency.
assert (
    # Case 1: Input string is empty or contains only spaces.
    # We check if the list of non-empty words derived from the input is empty.
    (not list(filter(None, test.split(" "))) and return_value == {})
    or
    # Case 2: Input string contains actual words.
    (
        # Ensure there are actual words in the input string.
        list(filter(None, test.split(" ")))
        and
        # Use nested lambda functions to create local "variables" in a functional style.
        # This calculates word frequencies and the maximum frequency from the input 'test'.
        (
            (lambda words_list:
                (lambda unique_words:
                    (lambda word_freqs_tuples:
                        (lambda max_freq_val:
                            # 1. All keys in 'return_value' must be present in the calculated
                            #    frequencies and their values must equal the maximum frequency.
                            all(k in map(lambda x: x[0], word_freqs_tuples) and return_value[k] == max_freq_val for k in return_value)
                            and
                            # 2. All words from the input that have the maximum frequency must
                            #    be present as keys in 'return_value'.
                            all(item[0] in return_value for item in word_freqs_tuples if item[1] == max_freq_val)
                            and
                            # 3. All values in 'return_value' must be equal to the maximum frequency.
                            all(v == max_freq_val for v in return_value.values())
                        )(
                            # Calculate the maximum frequency value from the word frequencies.
                            max(map(lambda item: item[1], word_freqs_tuples))
                        )
                    )(
                        # Create a list of (word, count) tuples for all unique words.
                        list(map(lambda w: (w, len(list(filter(lambda x: x == w, words_list)))), unique_words))
                    )
                )(
                    # Get a list of all unique non-empty words from 'words_list'.
                    # set() is used here to efficiently get unique elements.
                    list(set(words_list))
                )
            )(
                # Get a list of all non-empty words from the input string.
                list(filter(None, test.split(" ")))
            )
        )
    )
)


