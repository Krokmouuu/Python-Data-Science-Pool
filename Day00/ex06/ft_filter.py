

def ft_filter(func, object: any) -> any:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    newlist = [i for i in object if func(i) is True]
    return newlist


# def names_vowels(x): #Test Function
#   return x[0].lower() in 'aeiou'


def main():

    names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']
    names = ft_filter(lambda names: len(names) >= 5, names)  # My Function
    # names = list(filter(lambda names: len(names) >= 5, names))  #RealFunction
    print(names)
    return


if __name__ == "__main__":
    main()
