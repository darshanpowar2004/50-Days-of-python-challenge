# Day 48
# Binary Search

def binary_search(arr,x):
    low_index = 0
    high_index = len(arr)-1
    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        if arr[mid_index] == x:
            return mid_index
        elif arr[mid_index] > x:
            high_index = mid_index -1
        elif arr[mid_index] < x:
            low_index = mid_index + 1
    return "no element"

if __name__ == '__main__':
    list1 = [12, 34, 56, 78, 98, 22, 45, 13]
    list1 = sorted(list1)
    print(binary_search(list1,22))