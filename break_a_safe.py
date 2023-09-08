from itertools import permutations


def generate_permutations(iterable: list, digits: int) -> None:
    for p in permutations(iterable, digits):
        print(', '.join(map(str, p)))


def main() -> None:
    for i in [1, 5, 8]:
        generate_permutations([1, 5, 8, i], 4)


if __name__ == "__main__":
    main()
