def count_occurence_of_character(filename: str, char: str) -> int:
    # Counts the occurence of a character in text file
    try:
        with open(filename, 'r') as f:
            return f.read().count(char)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return -1
    except IOError:
        print(f"An error occurred while trying to read the file {filename}.")
        return -1
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}.")
        return -1

def main() -> None:
    print(count_occurence_of_character("lorem_ipsum.txt", 'e'))

if __name__ == "__main__":
    main()
