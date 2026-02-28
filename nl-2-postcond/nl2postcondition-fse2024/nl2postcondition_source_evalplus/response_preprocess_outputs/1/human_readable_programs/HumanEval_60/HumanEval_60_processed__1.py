def sum_to_n_original(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return (n + 1) * n // 2


def sum_to_n(n: int):


    return_value = sum_to_n_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    # This postcondition checks that the return_value is equal to the sum of integers from 1 to n, calculated using the arithmetic series formula.
    assert return_value == (n * (n + 1)) // 2

    return return_value
