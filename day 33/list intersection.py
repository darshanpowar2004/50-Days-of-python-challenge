# Day 33
# List Intersection

def inter_section(arr1 : list,arr2 : list):
    l1 = [x for x in arr1 if x in arr2]
    return tuple(l1)

if __name__ == '__main__':
    list1 = [20, 30, 60, 65, 75, 80, 85]
    list2 = [42, 30, 80, 65, 68, 88, 95]
    print(inter_section(list1,list2))