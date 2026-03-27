"""General decorators (alphabetically organized) to be used within python callables."""

import functools
import time
import typing as tp

# Type hinting setup
P = tp.ParamSpec("P")
T = tp.TypeVar("T")


def time_execution(func: tp.Callable[P, T]) -> tp.Callable[P, T]:
    """A decorator that measures and prints the execution time of a function.

    The decorator differs from the [`timeit`](https://docs.python.org/3/library/timeit.html)
    module as the module is defined to measure small bits of Python code (allowing
    multiple repetitions) while the decorator displays the runtime of the single
    decorated function.

    Examples
    --------
    ```pycon
    >>> from home_utils.decorators import time_execution
    >>> @time_execution
    ... def heavy_computation(n: int) -> list[int]:
    ...     return [i**2 for i in range(n)]
    >>> heavy_computation(50_000)
    Function 'heavy_computation' executed in 0.002569 seconds
    ```
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> T:
        start_time = time.perf_counter()
        # Execute the original function
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(
            f"Function '{func.__name__}' executed in "
            f"{end_time - start_time:.6f} seconds"
        )
        return result

    return wrapper
