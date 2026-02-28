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
    # The postcondition ensures that return_value is True if and only if there exists a split point in the string such that there are at least two opening brackets before the split and at least two closing brackets after the split, which is equivalent to the existence of a balanced subsequence with at least one nested bracket.
    assert return_value == any(string[:i].count('[') >= 2 and string[i:].count(']') >= 2 for i in range(len(string) + 1))

    return return_value
