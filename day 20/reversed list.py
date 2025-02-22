# Reversed List


def reversed_list(str1 : str):
    str1 = str1.replace(",","").split(" ")
    arr = []
    for word in str1:
        if not word.islower() or word.isupper():
            temp = word[::-1]
            arr.append(temp)

    return arr

if __name__ == "__main__":
    str1 = 'leArning is hard, bUt if You appLy youRself ' \
           'you can achieVe success'
    print(reversed_list(str1))