"""
A simple math calculator, supporting basic operations: adding,
subtracting, multiplying and division.
Well thanks for trying it out if you've cloned it :)
"""

from wrapping import *

SUPPORTED_OPERATOR = (
    "+",
    "-",
    "*",
    "/",
    "add",
    "subtract",
    "multiply",
    "divide",
)


def greet():
    print_with_line_seps(
        "Welcome to the math calculator, my first project ever!",
        "I'd appreciate if you try this calculator by yourself.",
        sep="\n",
    )


def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number:     "))
            num2 = float(input("Enter the second number:    "))
            return num1, num2
        except ValueError:
            print("Please type only integers or decimals")


def get_operator():
    while True:
        op = input(
            "Enter operator (+, -, *, /) or (add, subtract, multiply, divide):"
            # Extra indents
            "    "
        ).lower()

        if op in SUPPORTED_OPERATOR:
            return op

        print("Please choose from the options given!")


def calculate(num1, num2, op):
    match op:
        case "+" | "add":
            return num1 + num2
        case "-" | "subtract":
            return num1 - num2
        case "*" | "multiply":
            return num1 * num2
        case "/" | "divide":
            if num2 != 0:
                return num1 / num2
            else:
                print("Cannot divide a number by zero!")


def main():
    greet()

    while True:
        num1, num2 = get_numbers()
        op = get_operator()
        result = calculate(num1, num2, op)

        if result is not None:
            print_with_line_seps(f"Result: {num1} {op} {num2} = {result}")

        again = (
            input("Do you want to calculate again? (y/n): ").strip().lower()
        )
        if again != "y":
            print_with_line_seps(
                "Thanks for using my calculator, have a nice day!"
            )
            break


if __name__ == "__main__":
    main()
