def get_closest_vowel_original(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """

    def is_vowel(ch: str) -> bool:
        return ch in 'aeiouAEIOU'
    for i in range(len(word) - 2, 0, -1):
        if is_vowel(word[i]) and (not is_vowel(word[i - 1])) and (not is_vowel(word[i + 1])):
            return word[i]
    return ''


def get_closest_vowel(word):


    return_value = get_closest_vowel_original(word)
    
    # Adding imports that might be useful for postconditions
    import re 
    # This postcondition checks two cases for the function's return value:
    # 1. If the `return_value` is a single character, it asserts that this character is the rightmost vowel in the `word` that is
    #    surrounded by two consonants. This condition specifically excludes characters at the beginning and end of the `word`.
    # 2. If the `return_value` is an empty string, it asserts that no such vowel (a vowel surrounded by two consonants, not at the edges) exists in the `word`.
    def _is_vowel_postcondition(ch):
        return ch in "aeiouAEIOU"
    
    def _is_consonant_postcondition(ch):
        return ch.isalpha() and not _is_vowel_postcondition(ch)
    
    candidate_indices = [
        i for i in range(1, len(word) - 1)
        if _is_vowel_postcondition(word[i]) and _is_consonant_postcondition(word[i-1]) and _is_consonant_postcondition(word[i+1])
    ]
    
    assert (len(return_value) == 1 and candidate_indices and return_value == word[max(candidate_indices)]) or \
           (len(return_value) == 0 and not candidate_indices)

    return return_value
