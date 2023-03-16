# type(object) returns the type of the object
def all_thing_is_obj(object: any) -> int:
    if (type(object) == str):
        print(object + " is in the kitchen ", end='')
        print(type(object))
    elif (type(object) == list):
        print('List :', type(object))
    elif (type(object) == tuple):
        print('Tuple :', type(object))
    elif (type(object) == set):
        print('Set :', type(object))
    elif (type(object) == dict):
        print('Dict :', type(object))
    else:
        print("Type not found")
    return 42
