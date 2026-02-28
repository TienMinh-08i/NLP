def skjkasdkd_original(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """

    def is_prime(a):
        return not (a < 2 or any((a % x == 0 for x in range(2, int(a ** 0.5) + 1))))
    sorted_list = sorted(lst)[::-1]
    for x in sorted_list:
        if is_prime(x):
            return sum(map(lambda ch: int(ch), str(x)))


def skjkasdkd(lst):


    return_value = skjkasdkd_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that:
    # 1. If no prime numbers are found in the input list `lst`, then `return_value` must be `None`.
    # 2. If prime numbers are found, then `return_value` must be equal to the sum of the digits of the largest prime number in `lst`.
    assert (lambda ret_val, input_lst:
        # Helper lambda function to check if a number is prime
        (lambda is_prime_check:
            # Helper lambda function to calculate the sum of digits of a number
            (lambda sum_digits_func:
                # Filter the input list to get only prime numbers
                (lambda primes_found:
                    # Condition 1: If no primes are found in the list, the return value must be None.
                    (len(primes_found) == 0 and ret_val is None) or
                    # Condition 2: If primes are found, the return value must be the sum of digits of the largest prime.
                    (len(primes_found) > 0 and sum_digits_func(max(primes_found)) == ret_val)
                )(list(filter(is_prime_check, input_lst)))
            )(lambda num: sum(map(int, str(num)))) # sum_digits_func definition
        )(lambda n: not (n < 2 or any(n % x == 0 for x in range(2, int(n**0.5) + 1)))) # is_prime_check definition
    )(return_value, lst)

    return return_value
