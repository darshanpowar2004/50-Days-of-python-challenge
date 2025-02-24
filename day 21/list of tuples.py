# Day 21
# List Of Tuples

def make_tuples(arr1 : list , arr2 : list):
    if len(arr1) == len(arr2):
        new_list = []
        for i in range(len(arr1)):
            temp = (arr1[i],arr2[i])
            new_list.append(temp)

        return new_list
    else:
        return "Two list are not equal."

if __name__ == "__main__":
    arr1 = [1,2,3,4]
    arr2 = [5,6,7,8]
    output = make_tuples(arr1,arr2)
    print(output)
