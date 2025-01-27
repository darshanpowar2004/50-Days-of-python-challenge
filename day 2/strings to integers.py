# Strings to Integers

def convert_add(elements : list):
    for i in range(len(elements)):
        elements[i] = int(elements[i])

    return sum(elements)

if __name__ == "__main__":
    elements = ['1','3','5']
    total = convert_add(elements)
    print(elements)
    print(total)