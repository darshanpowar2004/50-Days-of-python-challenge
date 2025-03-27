import string


def analyse_string(a: str):
    output = {
        "words": 0,
        "numbers": 0,
        "whitespace": 0,
        "special_characters": 0,
        "total_characters": len(a)
    }

    special_char_set = set(string.punctuation)  # Using Python's punctuation set for special characters

    for x in a:
        if x.isalpha():
            output["words"] += 1
        elif x.isdigit():
            output["numbers"] += 1
        elif x.isspace():
            output["whitespace"] += 1
        elif x in special_char_set:
            output["special_characters"] += 1

    return output


if __name__ == '__main__':
    s = '''Python has a string format operator %. This functions 
    analogously to printf format strings in C, e.g. "spam=%s 
    eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".'''

    print(analyse_string(s))