# Length Of Words

def string_length(a : str):
    a = a.split(" ")
    str_dict = {}
    for word in a:
        str_dict[word] = len(word)

    return str_dict

if __name__ == '__main__':
    s = 'Hi my name is Richard'
    print(string_length(s))

