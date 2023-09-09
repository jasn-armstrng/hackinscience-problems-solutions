def valid_parentheses(string: str) -> bool:
    parentheses: dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    stack: list = []
    for char in string:
        if char in parentheses:
            stack.append(char)
        elif not stack or parentheses[stack.pop()] != char:
            return False
    return not stack

def test_valid_parentheses() -> None:
    assert valid_parentheses("()") is True
    assert valid_parentheses("()[]{}") is True
    assert valid_parentheses("(]") is False
    print("All test have passed")

def main() -> None:
    test_valid_parentheses()

if __name__ == "__main__":
    main()
