import string


def count_letters(filename: str) -> dict:
    """
    Counts the occurrence of each letter (case-insensitive) in the given file.

    Args:
    filename (str): Path to the file to analyze.

    Returns:
    dict: A dictionary where keys are letters and values are their counts.

    Raises:
    Exception: If an error occurred while reading the file.
    """
    letters = {letter: 0 for letter in string.ascii_lowercase}

    try:
        with open(filename, 'r') as file:
            for line in file:  # Rather than read whole file into memory, read line by line
                for char in line.lower():
                    if char in letters:
                        letters[char] += 1
    except Exception as e:
        print(f"An error occurred while trying to read the file {filename}. Error: {type(e).__name__}, {str(e)}")
        return None

    return letters


def letter_frequencies(filename: str) -> dict:
    """
    Calculate the frequency of each letter in the given file.

    Args:
    filename (str): Path to the file to analyze.

    Returns:
    dict: A dictionary where keys are letters and values are their frequencies.
    """
    letters = count_letters(filename)
    if letters is None:
        return None

    total_letters = sum(letters.values())
    frequencies = {letter: count / total_letters for letter, count in letters.items()}

    return frequencies


def main() -> None:
    frequencies = letter_frequencies("lorem_ipsum.tx")
    if frequencies is not None:
        for letter, frequency in frequencies.items():
            print(f'{letter}: {frequency:.2f}')


if __name__ == "__main__":
    main()
