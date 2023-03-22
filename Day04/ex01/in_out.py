def square(x: int | float) -> int | float:
    """Square"""
    if (x == 0 or x == 1):
        return x
    return x * x


def pow(x: int | float) -> int | float:
    """Power"""
    if (x == 0 or x == 1):
        return x
    return x**x


def outer(x: int | float, function) -> object:
    """Outer"""
    try:
        if (function != square and function != pow):
            raise TypeError("function must be square or pow")
        if (type(x) != int and type(x) != float):
            raise TypeError("x must be int or float")
        count = 0

        def inner() -> float:
            """Inner"""
            # nonlocal is used to read and write a variable in the outer scope
            nonlocal x, count
            if count == 0:
                count += 1
                return function(x)
            else:
                x = function(x)
                count += 1
                return function(x)
        return inner
    except TypeError as e:
        print("TypeError :", e)
        exit()
