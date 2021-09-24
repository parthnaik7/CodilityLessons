from time import time


def timeit(func):
    """
    This function shows the execution time of the function object passed
    """

    def wrap_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Function {func.__name__!r} executed in {(end - start):.4f}s')
        return result

    return wrap_func
