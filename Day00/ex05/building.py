import sys as arg


def print_final(upper: int, lower: int,
                digit: int, punct: int, space: int, total: int) -> None:
    """Print the final result"""
    total = upper + lower + digit + punct + space
    print("The text contains", total, "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punct, "punctuation marks")
    print(space, "spaces")
    print(digit, "digits")


def prompt_function() -> None:
    """Display a Prompt and waiting for input"""
    [upper := 0, lower := 0, digit := 0, ponct := 0, space := 0]
    punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n\t\r\b\f\0'
    print("What is the text to count?")
    string = arg.stdin.readline()
    for c in string:
        if (c.isupper() is True):
            upper += 1
        elif (c.islower() is True):
            lower += 1
        elif (c.isspace() is True):
            space += 1
        elif (c.isdigit() is True):
            digit += 1
        else:
            for b in punct:
                if (c == b):
                    ponct += 1
    total = upper + lower + digit + ponct + space
    print_final(upper, lower, digit, ponct, space, total)
    return


def main():
    [upper := 0, lower := 0, digit := 0, ponct := 0, space := 0]
    punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n\t\r\b\f'
    try:
        assert len(arg.argv) < 3, "more than one argument is provided"
        if (arg.argv is None):
            return 0
        if (len(arg.argv) == 1):
            prompt_function()
            return 0
        if (len(arg.argv) == 2):
            for c in arg.argv[1]:
                if (c.isupper() is True):
                    upper += 1
                elif (c.islower() is True):
                    lower += 1
                elif (c.isspace() is True):
                    space += 1
                elif (c.isdigit() is True):
                    digit += 1
                else:
                    for b in punct:
                        if (c == b):
                            ponct += 1
            total = upper + lower + digit + ponct + space
            print_final(upper, lower, digit, ponct, space, total)
    except AssertionError as msg:
        print("AssertionError:", msg)
        return 1
    return 0


if __name__ == "__main__":
    main()
