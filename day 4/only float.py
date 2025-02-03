
def only_float(a,b):
    if str(float(a)) == a and str(float(b)) == b:
        return 2
    elif str(float(a)) != a and str(float(b)) != b:
        return 0
    else:
        return 1


if __name__ == "__main__":
    a = input("Enter : ")
    b = input("Enter : ")

    result = only_float(a,b)
    print(result)

