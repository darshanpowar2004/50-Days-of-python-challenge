def check_duplicates(elements : list):
    temp = []
    for x in elements:
        if x not in temp:
            temp.append(x)
        else:
            return x

    return "No Duplicates"

if __name__ == "__main__":
    fruits = ['apple', 'orange', 'banana', 'apple']
    names = ['Yoda', 'Moses', 'Joshua', 'Mark']

    print(check_duplicates(fruits))
    print(check_duplicates(names))