# algorithm Sieve of Eratosthenes is
#     input: an integer n > 1.
#     output: all prime numbers from 2 through n.

#     let A be an array of Boolean values, indexed by integers 2 to n,
#     initially all set to true.

#     for i = 2, 3, 4, ..., not exceeding √n do
#         if A[i] is true
#             for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
#                 set A[j] := false

#     return all i such that A[i] is true.
from typing import List
import math

def sieve_of_erasthones(max_val: int):
    """
    This function implements the Sieve of Eratosthenes algorithm to find all primes
    less than the given number.

    Args:
        max_val: The upper limit up to which we want to find prime numbers.

    Returns:
        A list of Boolean values corresponding to indices up to max_val.
        A True value at index i indicates that i is a prime number.
    """
    max_val += 1
    # Initially set all numbers as prime (True)
    b_values = [True for i in range(max_val)]
    # 0 and 1 are not prime numbers
    b_values[0] = b_values[1] = False

    # Only need to consider numbers up to square root of max_val
    for i in range(2, int(math.sqrt(max_val)) + 1):
        # If the current number is prime
        if b_values[i]:
            # All multiples of this number are not prime
            # Cross off multiples of i starting from i*i, skipping even multiples
            for j in range(i*i, max_val, i*2 if i > 2 else i):
                b_values[j] = False

    return b_values


def is_prime(n: int) -> bool:
    primes = sieve_of_erasthones(n)
    return primes[n]


def main() -> None:
    print(type(sieve_of_erasthones(23)))



if __name__ == "__main__":
    main()
