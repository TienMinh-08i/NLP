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
    # The postcondition verifies that the returned string has the same length as the input string.
    # It then checks each character: if the original character is a lowercase letter, the corresponding returned character must be shifted by 4 positions (wrapping around the alphabet); otherwise, the returned character must be identical to the original.
    assert len(s) == len(return_value) and \
           all(char_s == char_r if not char_s.islower() else \
               ord(char_r) == (ord(char_s) - ord('a') + 4) % 26 + ord('a') \
               for char_s, char_r in zip(s, return_value))

    return return_value
