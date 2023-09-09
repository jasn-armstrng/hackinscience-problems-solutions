# https://www.hackinscience.org/exercises/flatten-lists
def flatten(input: list) -> list:
    """
    Flattens a nested list into a single list.

    This function takes as input a list that may contain sublists at any level of nesting.
    It returns a new list that contains all the elements of the original list but with
    all the nesting removed.

    The order of elements in the output list matches the order of elements in the input list,
    reading from left to right and from outer lists before inner lists.

    Args:
        lst (List): A list potentially containing sublists at any level of nesting. The sublists can
            contain any type of elements.

    Returns:
        List: A new list containing all the elements of the input list but with all the nesting removed.

    Example:
        >>> flatten([1, [2, [3, 4], 5]])
        [1, 2, 3, 4, 5]
    """
    flattened: list = []
    for i in input:
        if isinstance(i, list):
            flattened.extend(flatten(i))  # If the element is a list, make a recursive call
        else:  # Base case: the element is an individual item, not a list
            flattened.append(i)
    return flattened

def test_flatten() -> None:
    assert flatten([[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert flatten([[1, 2, [3]], 4, [5, [6, 7]]]) == [1, 2, 3, 4, 5, 6, 7]
    print("All test have passed")

def main() -> None:
    test_flatten()

if __name__ == "__main__":
    main()
