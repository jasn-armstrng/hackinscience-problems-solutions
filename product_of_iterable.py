from functools import reduce
from typing import List


def mul(nums: List[int]) -> int:
    '''
    Returns the product of all items in a list
    '''
    return reduce(lambda x, y: x * y, nums, 1)


def test_muls() -> None:
    assert mul([1, 2, 3]) == 6  # prints 6
    assert mul([0, 1, 2, 3]) == 0  # prints 0
    assert mul([2, 3, 4]) == 24 # prints the result of 2 * 3 * 4, being 24
    assert mul([2, 3, 4]) + mul([1, 2]) == 26  # prints the result of 2×3×4 + 1×2, which is 26
    print("All tests have passed.")


def main() -> None:
    test_muls()


if __name__ ==  "__main__":
    main()
