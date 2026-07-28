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

def log_history(expression, result):
    with open("history.txt", "a") as file:
        file.write(f"{expression},{result}\n")

def view_history():
    with open("history.txt", "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No history yet.")
    else:
        print("\n--- Calculation History ---")
        for line in lines:
            expression, result = line.strip().split(",")
            print(f"{expression} = {result}")

def clear_history():
    confirm = input("Are you sure you want to clear history? (y/n): ")
    if confirm == "y":
        with open("history.txt", "w") as file:
            pass
        print("History cleared.")
    else:
        print("Cancelled.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = operations.add(a, b)
            expression = f"{a} + {b}"
            log_history(expression, result)
            print(f"Result: {result}")

        elif choice == "2":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = operations.subtract(a, b)
            expression = f"{a} - {b}"
            log_history(expression, result)
            print(f"Result: {result}")

        elif choice == "3":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = operations.multiply(a, b)
            expression = f"{a} * {b}"
            log_history(expression, result)
            print(f"Result: {result}")

        elif choice == "4":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            try:
                result = operations.divide(a, b)
                expression = f"{a} / {b}"
                log_history(expression, result)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "5":
            base = get_number("Enter base: ")
            exponent = int(get_number("Enter exponent: "))
            try:
                result = operations.power(base, exponent)
                expression = f"{base} ^ {exponent}"
                log_history(expression, result)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "6":
            n = int(get_number("Enter a number: "))
            try:
                result = operations.factorial(n)
                expression = f"{n}!"
                log_history(expression, result)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "7":
            view_history()

        elif choice == "8":
            clear_history()
            
        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Not implemented yet.")


if __name__ == "__main__":
    main()