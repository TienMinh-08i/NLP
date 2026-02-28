def derivative_original(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [xs[i] * i for i in range(1, len(xs))]


def derivative(xs: list):


    return_value = derivative_original(xs)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition checks that return_value has a length of max(0, len(xs) - 1) and that each element at index i in return_value is equal to the element at index i + 1 in the input list xs multiplied by (i + 1).
    assert len(return_value) == max(0, len(xs) - 1) and all(return_value[i] == xs[i + 1] * (i + 1) for i in range(len(return_value)))

    return return_value
