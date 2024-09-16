import time

def cache(func):
    cache_store = {}
    def wrapper(*args, **kwargs):
        if args in cache_store:
            return cache_store[args]
        result = func(*args, *kwargs)
        cache_store[args] = result
        return result

    return wrapper

@cache
def long_running_func(a, b):
    time.sleep(4)
    return a + b

print(long_running_func(2, 3))
print(long_running_func(2, 3))
print(long_running_func(2, 4))