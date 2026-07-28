from operations import (
    add,
    clear_history,
    divide,
    factorial,
    multiply,
    power,
    read_history,
    save_history,
    subtract,
)


def prompt_number(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Please enter a valid number.")


def prompt_int(prompt_text):
    while True:
        try:
            return int(input(prompt_text))
        except ValueError:
            print("Please enter a valid whole number.")


def perform_binary_operation(operation_name, operation_func):
    first_number = prompt_number("Enter first number: ")
    second_number = prompt_number("Enter second number: ")

    try:
        result = operation_func(first_number, second_number)
    except ValueError as exc:
        print(f"Error: {exc}")
        return None

    expression = f"{first_number} {operation_name} {second_number}"
    save_history(expression, result)
    print(f"Result: {result}")
    return result


def perform_power():
    base = prompt_number("Enter base: ")
    exponent = prompt_int("Enter exponent: ")

    try:
        result = power(base, exponent)
    except ValueError as exc:
        print(f"Error: {exc}")
        return None

    expression = f"{base} ^ {exponent}"
    save_history(expression, result)
    print(f"Result: {result}")
    return result


def perform_factorial():
    number = prompt_int("Enter a non-negative integer: ")

    try:
        result = factorial(number)
    except ValueError as exc:
        print(f"Error: {exc}")
        return None

    expression = f"{number}!"
    save_history(expression, result)
    print(f"Result: {result}")
    return result


def show_history():
    entries = read_history()
    if not entries:
        print("No history yet.")
        return

    print("Calculation history:")
    for entry in entries:
        print(entry)


def clear_history_confirm():
    confirmation = input("Clear all history? (y/n): ").strip().lower()
    if confirmation == "y":
        clear_history()
        print("History cleared.")
    else:
        print("History was not cleared.")


def main():
    while True:
        print("\nCLI Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Factorial")
        print("7. View History")
        print("8. Clear History")
        print("9. Exit")

        choice = input("Choose an operation: ").strip()

        if choice == "1":
            perform_binary_operation("+", add)
        elif choice == "2":
            perform_binary_operation("-", subtract)
        elif choice == "3":
            perform_binary_operation("*", multiply)
        elif choice == "4":
            perform_binary_operation("/", divide)
        elif choice == "5":
            perform_power()
        elif choice == "6":
            perform_factorial()
        elif choice == "7":
            show_history()
        elif choice == "8":
            clear_history_confirm()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number from 1 to 9.")


if __name__ == "__main__":
    main()
