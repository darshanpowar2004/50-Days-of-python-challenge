# Reverse A String

def read_backwards( a : str):
    re_str = []
    for i in a.split(" ")[::-1]:
        re_str.append(i)

    return " ".join(re_str)



if __name__ == '__main__':
    str1 = 'the love is real'
    print(read_backwards(str1))