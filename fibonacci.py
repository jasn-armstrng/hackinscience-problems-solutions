# Fibonacci using Dynamic programming for a O(n) solution

from typing import List

def fibonacci(n: int) -> List[int]:
    """
    Generate the first n numbers of the Fibonacci sequence.

    Args:
        n: The length of the Fibonacci sequence to generate.

    Returns:
        A list of the first n numbers in the Fibonacci sequence.
        If n is 0, it returns an empty list.
        If n is 1 or more, it returns a list starting with [1, 1,...].

    """
    if n == 0:
        return []
    elif n == 1:
        return [1]

    sequence: List[int] = [1, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2]);  # Use previously calculated Fibonacci numbers to calculate the current one. Sum the last 2 entries in list.

    return sequence


def test_fibonacci() -> None:
    assert fibonacci(0) == []
    assert fibonacci(1) == [1]
    assert fibonacci(2) == [1, 1]
    assert fibonacci(3) == [1, 1, 2]
    assert fibonacci(5) == [1, 1, 2, 3, 5]
    assert fibonacci(7) == [1, 1, 2, 3, 5, 8, 13]
    print("All tests have passed")


def main() -> None:
    # print(fibonacci(1))
    test_fibonacci()


if __name__ == "__main__":
    main()
