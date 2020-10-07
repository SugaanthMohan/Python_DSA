# <<<<<<<<<<<<<<<<<< MODULES LIST >>>>>>>>>>>>>>>>>
# USED FOR DECORATOR CREATION
from functools import wraps
# TIME MODULE FOR TIME CALCULATION
import time


def seconds_benchmark(function_wrapper):
    """
    outer wrapper function to perform inner wrap for seconds benchmark.
    :param function_wrapper: The entire function object.
    :return:
    """

    @wraps(function_wrapper)
    def wrap(*args, **kwargs):
        """

        :param args: positional args
        :param kwargs: keyword args
        :return:
        """
        start_time = time.time()
        result = function_wrapper(*args, **kwargs)
        print("Function : %r | Args : %r | P-Args : %r | Elapsed Secs : %.3f Sec(s)"
              % (
                  function_wrapper.__name__, args, kwargs, time.time() - start_time
              )
              )
        return result

    return wrap
