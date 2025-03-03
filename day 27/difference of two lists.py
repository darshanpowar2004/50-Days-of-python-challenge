# Difference of Two Lists

def difference(arr1 : list,arr2 : list):
    a = [x for x in arr1 if x not in arr2]
    b = [x for x in arr2 if x not in arr1]
    return a+b

if __name__ == '__main__':
    list1 = [1,2,4,5,6]
    list2 = [1,2,5,7,9]
    print(difference(list1,list2))