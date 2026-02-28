def is_nested_original(string):
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    """
    for i in range(len(string)):
        if string[i] == ']':
            continue
        cnt, max_nest = (0, 0)
        for j in range(i, len(string)):
            if string[j] == '[':
                cnt += 1
            else:
                cnt -= 1
            max_nest = max(max_nest, cnt)
            if cnt == 0:
                if max_nest >= 2:
                    return True
                break
    return False


def is_nested(string):


    return_value = is_nested_original(string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition asserts that the return value is True if and only if there exists at least one substring of the input 'string'
    # that forms a valid, balanced bracket sequence with a maximum nesting depth of 2 or more.
    # A valid, balanced bracket sequence means that the balance of brackets (open minus close) never goes negative during traversal
    # and ends at zero.
    assert return_value == any(
        (lambda sub_string:
            (lambda balance_info:
                balance_info[0] == 0 and        # Final balance must be zero for a valid sequence
                not balance_info[2] and         # Balance must never have gone negative
                balance_info[1] >= 2            # Maximum nesting depth must be at least 2
            )
            (
                # functools.reduce is used to calculate the final balance, maximum depth, and whether balance ever went negative
                # for a given substring.
                # The accumulator (acc) stores a tuple: (current_balance, max_depth_so_far, has_balance_gone_negative_flag).
                __import__('functools').reduce(
                    lambda acc, char:
                        (
                            acc[0] + (1 if char == '[' else -1),  # Update current balance
                            max(acc[1], acc[0] + (1 if char == '[' else -1)), # Update max depth encountered
                            acc[2] or (acc[0] + (1 if char == '[' else -1) < 0) # Update flag if balance went negative
                        ),
                    sub_string,
                    (0, 0, False) # Initial state: (balance=0, max_depth=0, went_negative=False)
                )
            )
        )(string[i:j+1]) # Iterate through all possible substrings (string[i:j+1])
        for i in range(len(string))
        for j in range(i, len(string))
    )
    

    return return_value
