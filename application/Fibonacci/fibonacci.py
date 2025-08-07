'''
This is a module for the fibonacci function.
'''
import logging

# Configure basic logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def fibonacci(n: int) -> int:
    '''
    This function calculates the nth Fibonacci number using an iterative approach.
    Args:
        n (int): The position of the Fibonacci number to be calculated.
    Returns:
        int: The nth Fibonacci number.
    '''
    if n < 0:
        logger.error("Invalid input: n must be non-negative, got %d", n)
        raise ValueError("n must be a non-negative integer")

    a, b = 0, 1
    logger.debug("Starting computation for fibonacci(%d)", n)
    for j in range(n):
        logger.debug("Step %d: a=%d, b=%d", j, a, b)
        a, b = b, a + b

    logger.debug("Result: fibonacci(%d) = %d", n, a)
    return a

if __name__ == "__main__":
    # Example usage: print first 10 Fibonacci numbers
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")
