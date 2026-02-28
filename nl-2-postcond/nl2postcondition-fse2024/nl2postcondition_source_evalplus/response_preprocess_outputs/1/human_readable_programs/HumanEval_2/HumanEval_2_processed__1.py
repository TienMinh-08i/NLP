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
    # This postcondition asserts that the returned value is the exact decimal part of the input number, which is obtained by subtracting the largest integer less than or equal to the input number from the input number itself.
    assert return_value == number - int(number)

    return return_value
