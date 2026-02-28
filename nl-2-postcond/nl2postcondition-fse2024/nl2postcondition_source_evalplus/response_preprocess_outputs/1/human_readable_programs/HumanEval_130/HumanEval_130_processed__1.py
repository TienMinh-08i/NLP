def tri_original(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    if n == 0:
        return [1]
    if n == 1:
        return [1, 3]
    ans = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            ans.append(1 + i / 2)
        else:
            ans.append(ans[-1] + ans[-2] + 1 + (i + 1) / 2)
    return ans


def tri(n):


    return_value = tri_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    # This postcondition verifies that the returned list `return_value` has the correct length (`n + 1`) and that each element adheres to the Tribonacci sequence definition. Specifically, `return_value[0]` must be 1, `return_value[1]` must be 3, even-indexed elements `return_value[i]` (for `i >= 2`) must be `1 + i / 2`, and odd-indexed elements `return_value[i]` (for `i >= 3`) must be the sum of the two preceding elements and the value of the next element in the sequence, which for `i+1` (an even number) is `1 + (i + 1) / 2`.
    assert (len(return_value) == n + 1) and \
           all(
               (i == 0 and return_value[i] == 1) or \
               (i == 1 and return_value[i] == 3) or \
               (i >= 2 and i % 2 == 0 and return_value[i] == 1 + i / 2) or \
               (i >= 2 and i % 2 != 0 and return_value[i] == return_value[i - 1] + return_value[i - 2] + (1 + (i + 1) / 2))
               for i in range(n + 1)
           )

    return return_value
