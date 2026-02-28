# This postcondition verifies that the returned list `return_value` contains only valid number words (from "One" to "Nine"), and that when these words are converted back to numbers, the resulting numeric sequence matches the numbers from the input `arr` (filtered to be between 1 and 9 inclusive), sorted in descending order.
word_to_num_map = {
    "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5,
    "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9
}
assert (all(isinstance(x, str) and x in word_to_num_map for x in return_value) and
        list(map(lambda s: word_to_num_map[s], return_value)) ==
        sorted(list(filter(lambda x: 1 <= x <= 9, arr)))[::-1])


