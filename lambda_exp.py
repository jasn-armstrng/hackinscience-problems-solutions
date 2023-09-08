def filtered(iterable: list, filter) -> list:
    result: list = []
    for i in iterable:
        if filter(i):
            result.append(i)
    return result

def main() -> None:
    firstHundred = [i for i in range(0, 101)]
    for i in [3, 5, 15]:
        result = filtered(firstHundred, lambda x: x % i == 0)
        print(', '.join(map(str, result)))

if __name__ == "__main__":
    main()
