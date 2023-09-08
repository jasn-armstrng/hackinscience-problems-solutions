SQUARE_LENGTH: str = "+---"
SQUARE_MID: str    = "| 🪟 "


def draw_n_squares(n: int) -> str:
    """
    Prints a grid of squares of size 'n x n' to the console.

    Each square is represented by ASCII characters and has a dimension of 1x1.
    The top and bottom edges of the squares are represented by "+---",
    and the sides by "|   ",
    +---+
    |   |
    +---+
    The squares are arranged in a grid of 'n' rows and 'n' columns.


    Args:
        n (int): The number of squares in each row and column of the grid.
    """
    length: str = SQUARE_LENGTH * n + SQUARE_LENGTH[0]
    mid: str    = SQUARE_MID * n + SQUARE_MID[0]
    grid: str   = ""
    for _ in range(n):
        grid += f"{length}\n{mid}\n"
    grid += length

    return grid


def main() -> None:
    for i in range(6):
        print(draw_n_squares(i))


if __name__ == "__main__":
    main()
