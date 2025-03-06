# Sort by Last Name

def sorted_names(names : list):
    for i in range(len(names)):
        name = names[i].split(" ")
        names[i] = name[1] +" "+name[0]

    names.sort()


if __name__ == '__main__':
    names = ['Beyonce Knowles','Alicia Keys','Katie Perry','Chris Brown','Tom Cruise']
    sorted_names(names)
    print(names)