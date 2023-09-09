import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python3 solution.py PARAM")
        return
    params = [int(i) for i in sys.argv[1:]]
    print(sum(params))

if __name__ == "__main__":
    main()
