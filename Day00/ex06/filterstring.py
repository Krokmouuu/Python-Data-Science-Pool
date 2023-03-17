import sys as arg


def filterspring(string: str, n: int):
    """Filter the string and print the words with more than n characters"""
    newlist = [i for i in string.split() if string.split(' ')]
    newlist = list(filter(lambda string: len(string) > int(n), newlist))
    print(newlist)
    return


def main():
    try:
        assert len(arg.argv) == 3, "the arguments are bad"
        assert arg.argv[2].isdigit() is True, "the arguments are bad"
        filterspring(arg.argv[1], arg.argv[2])
    except AssertionError as msg:
        print("AssertionError:", msg)
    return 0


if __name__ == "__main__":
    main()
