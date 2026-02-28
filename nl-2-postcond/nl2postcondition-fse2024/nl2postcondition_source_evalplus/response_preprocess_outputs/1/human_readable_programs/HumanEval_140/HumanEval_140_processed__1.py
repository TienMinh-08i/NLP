def fix_spaces_original(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    ans = text
    for i in range(len(text) - 1, 2, -1):
        ans = ans.replace(' ' * i, '-')
    return ans.replace(' ', '_')


def fix_spaces(text):


    return_value = fix_spaces_original(text)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition asserts that the return_value is obtained by processing sequences of spaces in the original text.
    # Specifically, any block of 3 or more consecutive spaces is replaced by a single hyphen '-',
    # any block of 2 consecutive spaces is replaced by two underscores '__',
    # and any single space is replaced by one underscore '_'. Non-space characters and empty strings remain unchanged.
    assert return_value == "".join(
        [
            "-" if part.isspace() and len(part) >= 3
            else "__" if part.isspace() and len(part) == 2
            else "_" if part.isspace() and len(part) == 1
            else part
            for part in re.split(r'(\s+)', text)
        ]
    )
    

    return return_value
