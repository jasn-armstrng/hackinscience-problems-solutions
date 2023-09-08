import math
from typing import List


BLOCK = "\u2503"
EMPTY_INDICATOR = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def display(bars: int) -> str:
    """Displays a string representation of the battery."""
    indicator = EMPTY_INDICATOR.copy()  # Make a shallow copy
    for i in range(bars):
        indicator[i] = BLOCK
    return "".join(indicator)


def battery_charge(percentage: int) -> None:
    """
    Displays the battery charge graphically and in percentage.

    Args:
        percentage: A integer representing the battery charge percentage.
    """
    if percentage < 0 or percentage > 100:
        raise ValueError("Charge value must be in range [0, 100]")

    bars = round(percentage / 10)
    print(f"[{display(bars)}] {percentage}%\n")


def main() -> None:
    battery_charge(0)
    battery_charge(5)
    battery_charge(23)
    battery_charge(45)
    battery_charge(78)
    battery_charge(99)


if __name__ == "__main__":
    main()
