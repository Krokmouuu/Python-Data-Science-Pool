def callLimit(limit: int):
    """Decorator that limits the number of times a function can be called"""
    count = 0

    def callLimiter(function):
        """Returns a function that can only be called a limited times"""
        nonlocal count

        def limit_function(*args, **kwargs):
            """If func can be called, call it, otherwise print an error"""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print("Error:", function, "called too many times")
        return limit_function

    return callLimiter
