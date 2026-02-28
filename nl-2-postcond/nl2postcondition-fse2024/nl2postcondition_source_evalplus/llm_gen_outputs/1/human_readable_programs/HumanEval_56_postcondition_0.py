# The postcondition asserts that the function returns True if and only if two conditions are met:
# 1. The total number of opening brackets '<' equals the total number of closing brackets '>'.
# 2. At no point, when scanning the string from left to right, does the number of closing brackets exceed the number of opening brackets encountered so far.
assert return_value == (brackets.count('<') == brackets.count('>') and \
                        all(brackets[:i+1].count('<') >= brackets[:i+1].count('>') \
                            for i in range(len(brackets))))


