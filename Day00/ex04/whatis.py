import sys as arg


def main():
    try:
        size = len(arg.argv)
        if (size == 1):
            return 0
        assert size == 2, "more than one argument are provided"
        try:
            if (len(arg.argv) == 2):
                # f = arg.argv[1].isdigit()
                # assert f is True, "argument is not an integer"
                if (arg.argv[1][:0] == '-' or arg.argv[1][:0] == '+'):
                    num = arg.argv[1][:1].isdigit()
                    if (num is True):
                        raise AssertionError("argument is not an integer")
                    else:
                        num = int(arg.argv[1][1:])
                    if (num % 2 == 0):
                        print("I'm Even.")
                    else:
                        print("I'm Odd.")
                else:
                    num = arg.argv[1].isdigit()
                    if (num is True):
                        raise AssertionError("argument is not an integer")
                    else:
                        num = int(arg.argv[1])
                    if (num % 2 == 0):
                        print("I'm Even.")
                    else:
                        print("I'm Odd.")
        except AssertionError as msg:
            print("AssertionError:", msg)
    except AssertionError as msg:
        print("AssertionError:", msg)
    return


if __name__ == "__main__":
    main()
