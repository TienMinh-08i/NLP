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
    # The postcondition verifies that the length of the returned list of coefficients is correct (one less than the input list, or zero if the input was empty or a constant), and that each coefficient in the returned list is the product of the corresponding original coefficient and its original power.
    assert len(return_value) == max(0, len(xs) - 1) and all(return_value[j] == xs[j+1] * (j+1) for j in range(len(return_value)))

    return return_value
