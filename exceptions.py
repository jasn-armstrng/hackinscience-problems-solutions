import sys


def main() -> None:
    try:
        print(sys.argv[1])
    except IndexError:
        print("Not enough parameters.")
        sys.exit(1)


if __name__ == "__main__":
    main()
