import logging
import math
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def log_debug(message):
    """Log a message at DEBUG level."""
    logging.debug(message)

# dummy_repo/calculator.py

def add(a, b):
    return a + b

# keep the comments as it is
def subtract(a, b):
    return a - b

# New multiply function added
def multiply(*args):
    """Return the product of all provided numbers.

    Args:
        *args: A variable number of numeric arguments. At least one argument must be provided.

    Returns:
        The multiplication result of all arguments.
    """
    if not args:
        raise ValueError("multiply requires at least one argument")
    product = 1
    for number in args:
        product *= number
    return product
# New divide function added
def divide(a, b):
    """Return the result of dividing a by b.
    If b is zero, returns the string "Error: Division by zero".
    """
    if b == 0:
        return "Error: Division by zero"
    return a / b

# New modulo function added
def modulo(a, b):
    """Return the remainder of a divided by b.
    If b is zero, returns the string "Error: Division by zero".
    """
    if b == 0:
        return "Error: Division by zero"
    return a % b

# New power function added
def power(a, b):
    """Return a raised to the power of b.


def subtract(a, b):
    return a - b


def square(a):
    """Return the square of *a*.

    Parameters:
        a (numeric): The number to be squared.

    Returns:
        numeric: The result of *a* multiplied by itself.
    """
    log_debug(f"Calculating square for input: {a}")
    return a * a


if __name__ == "__main__":
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("3 squared =", square(3))
