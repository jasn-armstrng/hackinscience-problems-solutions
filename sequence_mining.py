from collections import Counter


def seq_mining(sequences: list[str], proportion: float, pattern_length: int) -> Counter:
    """
    Description:
        Extract common patterns among a set of sequences

    Parameters:
        1. A list of strings (representing the sequences)
        2. The minimum proportion of the number of sequences that must have this
           pattern for being taken into account (float between 0 and 1).
        3. The maximum pattern length that must be considered (int)

    Returns:
        A Counter object
    """
    counter = Counter()
    minimum_elements_having_pattern = round(len(sequences)/proportion)



    return counter


def test_seq_mining() -> None:
    data = ['ABCD', 'ABABC', 'BCAABCD']

    assert seq_mining(data, 0.34, 3) == Counter(
        {'A': 3,
         'AB': 3,
         'ABC': 3,
         'B': 3,
         'BC': 3,
         'BCD': 2,
         'C': 3,
         'CD': 2,
         'D': 2})

    assert seq_mining(data, 0.34, 4) == Counter(
        {'A': 3,
         'AB': 3,
         'ABC': 3,
         'ABCD': 2,
         'B': 3,
         'BC': 3,
         'BCD': 2,
         'C': 3,
         'CD': 2,
         'D': 2})

    assert seq_mining(data, 0.50, 2) == Counter(
        {'A': 3,
         'AB': 3,
         'B': 3,
         'BC': 3,
         'C': 3,
         'CD': 2,
         'D': 2})

    assert seq_mining(["ABC", "BCD"], 0.66, 2) == Counter(
       {'B': 2,
        'C': 2,
        'BC': 2})

    assert seq_mining(["ABC", "BCD"], 0.33, 2) == Counter(
       {'C': 2,
        'B': 2,
        'BC': 2,
        'A': 1,
        'D': 1,
        'AB': 1,
        'CD': 1})

    print("All tests have passed!")


def main() -> None:
    test_seq_mining()


if __name__ == "__main__":
    main()
