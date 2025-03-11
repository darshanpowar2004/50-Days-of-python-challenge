# Find My Position
def find_index(l : list,num : int):
    index_list = [i for i,x in enumerate(l) if x == num]

    if not index_list:
        index_list = [num] * len(l)

    return index_list

if __name__ == "__main__":
    arr  = [1, 2, 4, 6, 7, 7]
    num1 = 7
    num2 = 8
    print(find_index(arr,num1))
    print(find_index(arr,num2))