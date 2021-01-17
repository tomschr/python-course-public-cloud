# https://wiki.python.org/moin/PythonDecoratorLibrary#Function_Timeout

from functools import wraps
import signal
import time


def timeout(seconds: int,
            error_message: str = 'Function call timed out'):
    """
    Decorator to check if function exceeds a certain time.

    :param seconds: the time to wait before an error is raised
    :param error_message: the error message to output
    :raise TimeoutError: when the decorated function is too slow
    """
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        @wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wrapper

    return decorated


if __name__ == "__main__":
    @timeout(1, "Function was too slow, aborted")
    def slow_function():
        time.sleep(2)

    print("Before")
    try:
        slow_function()
    except TimeoutError as error:
        print("ERROR", error)
    print("After")
