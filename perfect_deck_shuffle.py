# Simulate a perfect suffle of a deck of cards.
# A perfect shuffle of a deck of card is splitting a deck of cards into equal halves, and perfectly interleaving them.
# Perfectly shuffling [1, 2, 3, 4, 5, 6] gives [1, 4, 2, 5, 3, 6].
# (We consider that a deck of cards has an even number of cards.)
from typing import List

def perfect_deck_shuffle(deck: List[int]) -> List[int]:
    """
    Performs a perfect shuffle on a deck of cards.

    A perfect shuffle involves splitting the deck into equal halves and perfectly interleaving them.

    Args:
        deck (List[int]): The deck to shuffle. Must have an even number of cards.

    Returns:
        List[int]: The shuffled deck.

    Raises:
        ValueError: If the deck has an odd number of cards.
    """
    if len(deck) % 2 != 0:
        raise ValueError("The deck must have an even number of cards.")

    mid: int = len(deck) // 2
    return [card for i in range(mid) for card in (deck[i], deck[i+mid])]


def test_perfect_deck_shuffle() -> None:
    assert perfect_deck_shuffle([1, 2, 3, 4]) == [1, 3, 2, 4]
    assert perfect_deck_shuffle([1, 2, 3, 4, 5, 6]) == [1, 4, 2, 5, 3, 6]
    assert perfect_deck_shuffle(['a', 'b', 'c', 'd', 'e', 'f']) == ['a', 'd', 'b', 'e', 'c', 'f']
    assert perfect_deck_shuffle([1, 3, 5, 7, 9, 11]) == [1, 7, 3, 9, 5, 11]
    assert perfect_deck_shuffle([10, 20, 30, 40]) == [10, 30, 20, 40]

    # Test with a single deck of cards (Ace=1, J=11, Q=12, K=13 for each suit)
    deck = list(range(1, 53))  # Generate a deck
    shuffled_deck = perfect_deck_shuffle(deck)  # Shuffle the deck
    # Check that the first card of the shuffled deck is 1
    # and the second card is the first card of the second half of the deck (27)
    assert shuffled_deck[0] == 1 and shuffled_deck[1] == 27

    print("All tests have passed")


def main() -> None:
    test_perfect_deck_shuffle()


if __name__ == "__main__":
    main()
