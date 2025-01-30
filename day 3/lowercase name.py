def lowercase_tuple(elements):
    temp = []
    for i in elements:
        if i.islower():
            temp.append(i)

    temp.sort(reverse=True)
    lowercase = tuple(temp)
    return lowercase


if __name__ == "__main__":
    names = ["aman","kerry", "dickson", "John", "Mary",
             "carol", "Rose", "adam"]

    output = lowercase_tuple(names)
    print(output)