from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Code to call before calling the decorated function

        # Call decorated function
        # Return it's results if needed
        return func(*args, **kwargs)
    
        # Code to execute instead of calling the decorated function

    return wrapper
