# https://www.hackinscience.org/exercises/longest-collatz-sequence

# The Collatz conjecture applies to +ve integers and speculates
# that it is always possible to get "back to 1" if you follow
# these steps
#    * If n is 1, stop
#    * Otherwise, if n is even, repeat this process on n / 2
#    * Otherwise, if n is odd, repeat this process on 3n + 1

def collatz_length(n: int) -> int:
    if n == 1:  # Base case. Terminate recursion
        return 0

    if n % 2 == 0:  # Recursive case
        return 1 + collatz_length(n/2)
    else:
        return 1 + collatz_length(3 * n + 1)

def test_collatz_length() -> None:
    assert collatz_length(10) == 6
    print("All tests have passed")

def main() -> None:
    test_collatz_length()

if __name__ == "__main__":
    main()
