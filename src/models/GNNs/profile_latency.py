import time
import functools

import logging

LOG_DIR='/scratch/ns_ksinha45/graphllms/GLEM-baseline/logs'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler(f'{LOG_DIR}/gnn_latency.log'))

LOG = True

def timer(func):
    """
    A decorator that prints the execution time of the decorated function
    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        # breakpoint()
        # if LOG:
        #     logger.debug(f"Function {func.__name__!r} took {run_time:.4f} seconds to complete")
        logger.debug(f"Function {func.__name__!r} took {run_time:.4f} seconds to complete")
        # else:
        #     print(f"Function {func.__name__!r} took {run_time:.4f} seconds to complete")
        return result
    return wrapper_timer

@timer
def example():
    a = 0
    for i in range(1_000_000):
        a += 1
    
if __name__ == "__main__":
    example()
    