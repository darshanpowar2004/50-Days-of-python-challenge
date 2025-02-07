def zeroed(elements : list):
    for i in range(len(elements)):
        elements[i] = int(elements[i])

    elements[0]=elements[-1]=0

if __name__ == '__main__':
    user = list(input("enter (use ,): ").split(","))
    zeroed(user)
    print(user)
