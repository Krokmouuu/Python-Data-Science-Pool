import numpy as numpy


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate the BMI of a person"""
    try:
        if (type(height) != list or type(weight) != list):
            raise AssertionError("Height or weight are not lists")
        if (type(height) == list and type(weight) == list):
            if (len(height) != len(weight)):
                raise AssertionError("H and W are not the same length")
            bmi = [weight[i] / (height[i] ** 2) for i in range(len(height))]
            return bmi
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI"""
    try:
        if (type(limit) != int):
            raise AssertionError("Limit is not an integer")
        newlist = numpy.array(bmi) > limit  # Apply the limit
        newlist = newlist.tolist()  # Convert the array to a list
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit()
    return newlist
