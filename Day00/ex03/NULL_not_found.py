def NULL_not_found(object: any) -> int:
    if (object is None):
        print("Nothing: None", type(object))
        return 0
    elif (type(object) == float and object == "NaN"):
        print("Cheese: nan", type(object))
        return 0
    elif (type(object) == bool and object is False):
        print("Fake: False", type(object))
        return 0
    elif (type(object) == int and object == 0):
        print("Zero: 0", type(object))
        return 0
    elif (type(object) == str and object == ""):
        print("Empty:", type(object))
        return 0
    else:
        print("Type not Found")
        return 1
