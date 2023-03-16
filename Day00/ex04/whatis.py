import sys as arg


def main():
    try:
        size = len(arg.argv)
        if (size == 1):
            return 0
        assert size == 2, "more than one argument are provided"
        if (len(arg.argv) == 2):
            f = arg.argv[1].isdigit()
            assert f is True, "argument is not an integer"
            num = int(arg.argv[1])
            if (num % 2 == 0):
                print("I'm Even.")
            else:
                print("I'm Odd.")
    except AssertionError as msg:
        print("AssertionError:", msg)
        return


if __name__ == "__main__":
    main()
