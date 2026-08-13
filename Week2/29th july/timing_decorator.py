#timing decorator
import time


def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Execution Time: {end - start:.6f} seconds")

        return result

    return wrapper


@timer
def display_numbers():

    for i in range(1, 500):
        pass

    print("Loop Completed")


display_numbers()