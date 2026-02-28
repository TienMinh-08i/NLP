def encrypt_original(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    d = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(map(lambda ch: chr((ord(ch) - ord('a') + 4) % 26 + ord('a')) if ch in d else ch, s))


def encrypt(s):


    return_value = encrypt_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that return_value has the same length as the input string s and that each lowercase character in s is shifted forward by 4 positions in the alphabet (cyclically), while all other characters remain unchanged.
    assert len(return_value) == len(s) and all(c_out == (chr((ord(c_in) - ord('a') + 4) % 26 + ord('a')) if 'a' <= c_in <= 'z' else c_in) for c_in, c_out in zip(s, return_value))

    return return_value
