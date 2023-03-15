import sys


def main():
    try :
        size = len(sys.argv)
        if (size == 1):
            return 0
        assert size == 2, "more than one argument are provided"
        if (len(sys.argv) == 2):
            f = sys.argv[1].isdigit()
            assert f != False, "argument is not an integer"
            num = int(sys.argv[1])
            if (num % 2 == 0):
                print("I'm Even.")
            else:
                print("I'm Odd.")
    except AssertionError as msg:
        print("AssertionError:", msg)

if __name__ == "__main__":
    main()