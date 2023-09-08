"""
Simple Calculator
Author: Your Name
Date: The current date
Version: The current version number of your program

This program is a simple command-line calculator. It supports basic arithmetic operations including
addition, subtraction, multiplication, division, exponentiation, and modulo operation.

The calculator is invoked from the command line with three arguments: two numbers and an operator.
The operator must be one of the following symbols: +, -, *, /, ^, %.

For example, to add 5 and 3, you would run: `python3 simple_calculator.py 5 + 3`
This would output: 8

Note: For division and modulo operations, the second number must not be zero.

The program includes error handling to ensure the operator is valid and to prevent division by zero.
If the user provides an unsupported operator or tries to divide by zero, the program prints an error
message and exits with status code 1.
"""
import sys
from typing import List


def add(operand_1: int, operand_2: int) -> int:
    """Perform addition."""
    return operand_1 + operand_2


def subtract(operand_1: int, operand_2: int) -> int:
    """Perform subtraction."""
    return operand_1 - operand_2


def multiply(operand_1: int, operand_2: int) -> int:
    """Perform multiplication."""
    return operand_1 * operand_2


def divide(operand_1: int, operand_2: int) -> float:
    """Perform division."""
    if operand_2 == 0:
        print("Error: Division by zero.")
        sys.exit(1)
    return operand_1 / operand_2


def power(operand_1: int, operand_2: int) -> int:
    """Perform exponentiation."""
    return operand_1 ** operand_2


def modulo(operand_1: int, operand_2: int) -> int:
    """Perform modulo operation."""
    if operand_2 == 0:
        print("Error: Modulo operation by zero.")
        sys.exit(1)
    return operand_1 % operand_2


OPERATION_FUNCTION_REF = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': power,
    '%': modulo
}


def calculate(input: List[str]) -> None:
    """Perform the operation specified in the input."""
    operation = OPERATION_FUNCTION_REF.get(input[1])
    if operation is None:
        print(f"Error: Unsupported operator '{input[1]}'")
        sys.exit(1)
    return (operation(int(input[0]), int(input[2])))


def test_calculate():
    # Test addition
    assert add(2, 3) == 5, "Addition test failed"

    # Test subtraction
    assert subtract(5, 3) == 2, "Subtraction test failed"

    # Test multiplication
    assert multiply(4, 3) == 12, "Multiplication test failed"

    # Test division
    assert divide(10, 2) == 5.0, "Division test failed"

    # Test power
    assert power(2, 3) == 8, "Power test failed"

    # Test modulo
    assert modulo(10, 3) == 1, "Modulo test failed"

    print("All tests passed!")


def main() -> None:
    """Entry point of the program."""
    if len(sys.argv) != 4:
        print("usage: ./simple_calculator.py a_number (an_operator +-*/%^) a_number")
        sys.exit(1)

    input: List[str] = sys.argv[1:]

    result = calculate(input)

    print(result)


if __name__ == "__main__":
    # test_calculate()
    main()
