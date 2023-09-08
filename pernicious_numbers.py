from math import sqrt
from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
    n : int : The number to check.

    Returns:
    bool : True if the number is prime, False otherwise.
    """

    # If the number is less than 2, it's not prime.
    if n < 2:
        return False

    # Check if the number is greater than 2 and even.
    # If so, it's not prime.
    # Note: We use bitwise AND operation with 1 to check for evenness.
    # This operation checks the least significant bit of `n`.
    # If it's 0, `n` is even; if it's 1, `n` is odd.
    # This method is faster than using modulo, especially for larger numbers.
    if n > 2 and n & 1 == 0:
        return False

    # If the number is not divisible by any number up to its square root, it's prime.
    for x in range(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True


def pernicious_numbers(range_: range) -> List[int]:
    """
    Find pernicious numbers in a range.

    A pernicious number is a positive integer where the count of '1's in its binary
    representation is a prime number.

    Args:
    range_ : range
        The range of numbers to check.

    Returns:
    List[int]
        A list of the pernicious numbers in the range.
    """
    pernicious_nums = []
    for i in range_:
        # Check if the number of 1s in the binary representation of i is prime
        if is_prime(bin(i).count('1')):
            pernicious_nums.append(i)

    return pernicious_nums


def main() -> None:
    pernicious_nums = pernicious_numbers(range(222281, 222381))
    for num in pernicious_nums:
        print(num)


if __name__ == "__main__":
    main()
