# https://www.hackinscience.org/exercises/print-sorbet-flavors
from itertools import combinations

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

def main() -> None:
    for combination in combinations(FLAVORS, 2):
        a, b = combination
        print(f"{a}, {b}")

if __name__ == "__main__":
    main()
