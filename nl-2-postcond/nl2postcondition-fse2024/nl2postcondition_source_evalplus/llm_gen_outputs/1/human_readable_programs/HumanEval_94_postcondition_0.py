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


