def NULL_not_found(object: any) -> int:
    if (object is None):
        print("Nothing: None", type(object))
    elif (type(object) == float):
        print("Cheese: nan", type(object))
    elif (type(object) == int):
        print("Zero: 0", type(object))
    elif (type(object) == str and object != "Brian"):
        print("Empty:", type(object))
    elif (type(object) == bool and object is False):
        print("Fake: False", type(object))
    elif (type(object) == str and object == "Brian"):
        print("Type not Found")
        return 1
    return 0
