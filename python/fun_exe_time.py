import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Time taken by function {func.__name__}: {end_time - start_time:.5f} seconds")
        return result
    return wrapper
@time_it
def my_function():
    # add your function code here
    time.sleep(2)

my_function()
