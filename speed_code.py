from time import time
from functools import wraps


def speed_test(functions):
    @wraps(functions)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = functions(*args, **kwargs)
        end_time = time()
        print(f'Time: {end_time-start_time}')
        return result
    return wrapper


@speed_test
def main():
    # write your code here
    pass
