import sys as arg


DICTIONARY = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '/'
}


def morse_translate(string: str):

    """Translate a string into morse code"""
    translated_text = ''
    for letter in string:
        if letter != ' ':
            translated_text += DICTIONARY[letter.upper()] + ' '
        elif letter == ' ':
            translated_text += '/' + ' '
    translated_text = translated_text[:-1]
    print(translated_text)


def main():
    try:
        assert len(arg.argv) == 2, "the arguments are bad"
    except AssertionError as msg:
        print("AssertionError:", msg)
        return
    morse_translate(arg.argv[1])
    return


if __name__ == '__main__':
    main()
