import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def log_debug(message):
    """Log a message at DEBUG level."""
    logging.debug(message)


def add(a, b):
    return a + b


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
