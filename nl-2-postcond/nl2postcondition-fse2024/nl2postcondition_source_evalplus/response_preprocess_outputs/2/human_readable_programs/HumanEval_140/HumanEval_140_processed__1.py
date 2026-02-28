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
    
    # The postcondition checks that return_value replaces all maximal blocks of three or more spaces with a hyphen 
    # and other spaces with underscores, while correctly handling the specific behavior of the code's 
    # loop when the entire string consists of spaces.
    import re
    assert return_value == (re.sub(r' {3,}', '-', text).replace(' ', '_') if text != ' ' * len(text) else ('-_' if len(text) > 3 else '_' * len(text)))
    

    return return_value
