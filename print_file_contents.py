def print_file_contents(filename: str) -> None:
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except IOError:
        print(f"There was an error opening or reading the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def main() -> None:
    print_file_contents('sets_of_love.py')


if __name__ == "__main__":
    main()
