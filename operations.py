from pathlib import Path


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def power(base, exponent):
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def save_history(expression, result, history_path=None):
    if history_path is None:
        history_path = Path(__file__).with_name("history.txt")
    else:
        history_path = Path(history_path)

    with history_path.open("a", encoding="utf-8") as handle:
        handle.write(f"{expression},{result}\n")


def read_history(history_path=None):
    if history_path is None:
        history_path = Path(__file__).with_name("history.txt")
    else:
        history_path = Path(history_path)

    if not history_path.exists():
        return []

    with history_path.open("r", encoding="utf-8") as handle:
        return [line.strip() for line in handle if line.strip()]


def clear_history(history_path=None):
    if history_path is None:
        history_path = Path(__file__).with_name("history.txt")
    else:
        history_path = Path(history_path)

    if history_path.exists():
        history_path.unlink()
