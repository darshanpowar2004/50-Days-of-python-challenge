# Add and Reverse

def add_reverse(arr1 : list,arr2 : list):
    if len(arr1) == len(arr2):
        new_list = []
        for i in range(len(arr1)):
            new_list.append(arr1[i] + arr2[i])
            new_list.reverse()
        # new_list = list(new_list.__reversed__())
        # them = new_list[1]
        # new_list[1] = new_list[-1]
        # new_list[2] = them

        return new_list
    else:
        return  "the lists are not of equal lengths"


if __name__ == '__main__':
    num1 = [10, 12, 34]
    num2 = [12, 56, 78]

    result = add_reverse(num1,num2)

    print(result)