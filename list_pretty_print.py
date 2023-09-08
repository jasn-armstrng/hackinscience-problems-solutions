# A function named list_pretty_print, taking a single parameter: a list of integers.
# Your function should display 5 integers per line (maximum), separated by ', '
# (coma space).
from typing import List


def list_pretty_print(integers: List[int]) -> None:
    output: str = ""
    for index, value in enumerate(integers):
        output += str(value)
        if (index+1) % 5 == 0:
            output += '\n'
        else:
            output += ", "

    print(output)


def main() -> None:
    list_pretty_print([42, 42, 42, 42, 42, 42])


if __name__ == "__main__":
    main()
