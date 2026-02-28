def x_or_y_original(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    def is_prime(a):
        return not (a < 2 or any((a % x == 0 for x in range(2, int(a ** 0.5) + 1))))
    return x if is_prime(n) else y


def x_or_y(n, x, y):


    return_value = x_or_y_original(n, x, y)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that return_value equals x if n is prime (n >= 2 and has no divisors from 2 up to its square root) and equals y otherwise.
    assert return_value == (x if (n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))) else y)

    return return_value
