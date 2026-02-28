def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    groups = [s[3 * i:min(3 * i + 3, len(s))] for i in range((len(s) + 2) // 3)]
    groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    return ''.join(groups)

def decode_cyclic_original(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[3 * i:min(3 * i + 3, len(s))] for i in range((len(s) + 2) // 3)]
    groups = [group[2] + group[:2] if len(group) == 3 else group for group in groups]
    return ''.join(groups)


def decode_cyclic(s: str):


    return_value = decode_cyclic_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition verifies that re-encoding the return_value by cycling its groups of three characters (moving the first character of each triplet to the end) results in the original encoded string s.
    assert "".join([(return_value[3 * i + 1 : 3 * i + 3] + return_value[3 * i : 3 * i + 1]) if len(return_value[3 * i : 3 * i + 3]) == 3 else return_value[3 * i : 3 * i + 3] for i in range((len(return_value) + 2) // 3)]) == s
    

    return return_value
