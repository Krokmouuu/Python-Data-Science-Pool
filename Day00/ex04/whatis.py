import sys as arg


def main():
    try:
        c = "-+"
        num = None
        if (len(arg.argv) == 1):
            return 0
        assert len(arg.argv) == 2, "more than one argument are provided"
        for i in c:
            if (i in arg.argv[1][0:]):
                if (len(arg.argv[1][1:]) > 1):
                    assert arg.argv[1][1:].isdigit(), "argument is not an integer"
                elif (i == "%"):
                    assert arg.argv[1][0:].isdigit(), "argument is not an integer"
                num = 0
        if (num == None):
            assert arg.argv[1].isdigit(), "argument is not an integer"
        num = int(arg.argv[1])
        if (num % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as error:
        print("AssertionError:", error)
        return 1
    return 0


if __name__ == "__main__":
    main()
