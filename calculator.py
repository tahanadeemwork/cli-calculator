import operations


def display_menu():
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


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = operations.add(a, b)
            print(f"Result: {result}")

        elif choice == "2":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = operations.subtract(a, b)
            print(f"Result: {result}")

        elif choice == "3":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = operations.multiply(a, b)
            print(f"Result: {result}")

        elif choice == "4":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            try:
                result = operations.divide(a, b)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Not implemented yet.")


if __name__ == "__main__":
    main()