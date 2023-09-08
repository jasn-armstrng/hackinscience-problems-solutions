from math import sqrt


def is_prime(n: int):
    if n < 2:
        return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(9) == False
    assert is_prime(7) == True
    assert is_prime(13) == True
    assert is_prime(33) == False
    print("All tests have passed")


def main() -> None:
    test_is_prime()


if __name__ == "__main__":
    main()
