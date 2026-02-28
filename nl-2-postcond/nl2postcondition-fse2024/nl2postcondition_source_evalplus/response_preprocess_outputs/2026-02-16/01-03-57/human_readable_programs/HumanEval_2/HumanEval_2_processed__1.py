def truncate_number_original(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


def truncate_number(number: float) -> float:


    return_value = truncate_number_original(number)
    
    # Adding imports that might be useful for postconditions
    import re 
    # This postcondition asserts that the returned value is the decimal part of the input number, meaning it's non-negative and less than 1, and when subtracted from the original number, the result is an integer.
    assert 0 <= return_value < 1 and (number - return_value) == int(number - return_value)

    return return_value
