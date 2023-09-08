import string

def main() -> None:
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            print(f"{i}{j}")


if __name__ == "__main__":
    main()
