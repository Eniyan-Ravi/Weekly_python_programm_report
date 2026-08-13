#logging decorator
import logging

logging.basicConfig(level=logging.INFO)


def logger(func):

    def wrapper(*args, **kwargs):

        logging.info(f"Executing {func.__name__}")

        result = func(*args, **kwargs)

        logging.info("Execution Completed")

        return result

    return wrapper


@logger
def multiply(a, b):

    return a * b


print("Result:", multiply(5, 8))