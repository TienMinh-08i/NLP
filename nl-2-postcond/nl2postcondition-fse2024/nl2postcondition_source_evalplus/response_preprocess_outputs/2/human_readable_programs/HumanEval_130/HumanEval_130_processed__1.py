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
    
    # The postcondition verifies that return_value has length n + 1, its first element is 1, its second element is 3 (if n >= 1), and all subsequent elements at index i follow the Tribonacci sequence: tri_original(i) = 1 + i/2 for even i, and tri_original(i) = tri_original(i-1) + tri_original(i-2) + 1 + (i+1)/2 for odd i.
    assert len(return_value) == n + 1 and return_value[0] == 1 and (n < 1 or return_value[1] == 3) and all(return_value[i] == (1 + i / 2 if i % 2 == 0 else return_value[i-1] + return_value[i-2] + 1 + (i + 1) / 2) for i in range(2, n + 1))
    

    return return_value
