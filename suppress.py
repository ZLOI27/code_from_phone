def suppress(exception_var, or_return=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_var:
                return or_return
        return inner
    return wrapper

