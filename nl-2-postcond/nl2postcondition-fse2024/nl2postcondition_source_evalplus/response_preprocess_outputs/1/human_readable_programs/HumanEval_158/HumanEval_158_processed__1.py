def find_max_original(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    mx_ch_cnt, ans = (0, '')
    for word in words:
        ch_cnt = len(set(word))
        if ch_cnt > mx_ch_cnt or (ch_cnt == mx_ch_cnt and word < ans):
            mx_ch_cnt, ans = (ch_cnt, word)
    return ans


def find_max(words):


    return_value = find_max_original(words)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that the returned value `return_value` is one of the words from the input list `words`, and it satisfies two conditions:
    # 1. No other word in `words` has more unique characters than `return_value`.
    # 2. Among all words that have the same maximum number of unique characters as `return_value`, `return_value` is the lexicographically smallest.
    assert all(len(set(return_value)) >= len(set(w)) for w in words) and all(return_value <= w for w in words if len(set(w)) == len(set(return_value)))

    return return_value
