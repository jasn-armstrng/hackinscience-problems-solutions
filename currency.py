# The function how_to_pay(amount: int, currency: List[int]) -> dict: is designed
# to find the easiest way to pay a certain amount with given denominations. The
# idea behind this function is a greedy algorithm: it tries to use the largest
# denomination that does not exceed the remaining balance.
from collections import defaultdict
from rich.console import Console
from typing import List


console = Console()


def how_to_pay(amount: int, currency: List[int]) -> dict:
    """
    Calculates the easiest way to pay a certain amount with given denominations.

    This function uses a greedy algorithm to find the minimum number of coins or
    banknotes to make up the given amount. It starts with the largest denomination
    and works its way down. The function will raise a ValueError if it is not possible
    to pay the exact amount with the given denominations that are less than or equal to
    the amount.

    Args:
        amount (int): The amount to pay. Must be non-negative.
        currency (List[int]): List of available denominations. Each denomination must be non-negative.

    Returns:
        dict: A dictionary where the keys are the denominations used and the values
        are the quantity of each denomination used to pay the amount.

    Raises:
        ValueError: If it's impossible to pay the exact amount with the given currency
        using denominations less than or equal to the amount.
        ValueError: If the amount or any of the denominations are negative.
    """
    if amount < 0:
        raise ValueError("Amount to pay must be non-negative.")
    if any(coin < 0 for coin in currency):
        raise ValueError("All currency values must be non-negative.")

    currency.sort(reverse=True)  # (O(n log n)). No control o'er the input, this sorting step is necessary.
    pay_with = defaultdict(int)

    while amount > 0:
        for i in currency:
            if i <= amount:
                amount -= i
                pay_with[i] += 1  # Direct increment, no need to check key existence
                break
        else:  #  while-loop without a definite end could potentially lead to an infinite loop if no suitable denomination is found.
            raise ValueError(f"Cannot pay the exact amount {amount} with the given currency using denominations less than or equal to the amount.")

    return pay_with


def test_how_to_pay() -> None:
    assert how_to_pay(3, [1, 2, 5]) == {2: 1, 1: 1}
    assert how_to_pay(1, [1, 5]) == {1: 1}
    assert how_to_pay(500, [1, 2, 5, 10, 20, 50, 100, 200, 500]) == {500: 1}
    assert how_to_pay(123, [1, 2, 5, 10, 20, 50, 100, 200, 500]) == {100: 1, 20: 1, 2: 1, 1: 1}
    assert how_to_pay(100, [50, 20, 10, 5]) == {50: 2}
    assert how_to_pay(2, [1, 2, 5, 10, 20, 50, 100, 200, 500]) == {2: 1}
    console.log("All tests have passed")


def main() -> None:
    test_how_to_pay()


if __name__ == "__main__":
    main()
