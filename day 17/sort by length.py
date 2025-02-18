# Sort By length

def sort_length(arr : list):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if len(arr[i]) > len(arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr



if __name__ == '__main__':
    names = ["Peter", "Jon", "Andrew","k","rahul","mahesh","om"]
    sorted_list = sort_length(names)
    print(sorted_list)