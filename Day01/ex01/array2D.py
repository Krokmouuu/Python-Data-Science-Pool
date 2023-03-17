import numpy as numpy

def slice_me(family: list, start: int, end: int) -> list:
    """Slice the list family from start to end"""
    try:
        tmp = str(start)
        tmp2 = str(end)
        for i in range(len(family)):
            if type(family[i]) is not list:
                raise AssertionError("family[{}] is not a list".format(i))
        for i in family:
            if len(i) != len(family[0]):
                raise AssertionError("family[{}] is not the same length as family[0]".format(i))
        print("My shape is : {}".format(numpy.shape(family)))
        print("My new shape is : {}".format(numpy.shape(family[start:end])))
        newlist = family[start:end]
        return newlist
    except AssertionError as error:
        print("AssertionError:", error)
        exit()
