def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}"for k, v in kwargs.items())
        print(f"{func.__name__} function calls these arguments {args_value} and calls key value arguments {kwargs_value}")
        return func(*args, *kwargs)
    return wrapper

@debug
def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")

greet("Rahul", greeting="Hi")