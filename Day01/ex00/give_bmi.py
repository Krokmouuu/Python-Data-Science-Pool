import numpy as numpy

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Calculate the BMI of a person"""
    try:
        if (type(height) == list and type(weight) == list):
            if (len(height) != len(weight)):
                raise AssertionError("Height and weight are not the same length")
            bmi = [weight[i] / (height[i] ** 2) for i in range(len(height))] # Calculate the BMI
            return bmi
        else:
            AssertionError("Height or weight are not lists")
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit()

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI"""
    if (limit != int):
        print("dd")
    newlist = numpy.array(bmi) > limit # Apply the limit
    newlist = newlist.tolist() # Convert the array to a list
    return newlist