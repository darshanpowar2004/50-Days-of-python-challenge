# Largest Number

def largest_num(arr : list):
    arr1 = "".join(map(str,arr))
    arr2 = list(map(int,arr1))
    arr2.sort(reverse=True)
    largest = int("".join(map(str,arr2)))

    return f"{largest:,}"

if __name__ == '__main__':
    list1 = [3,67,87,9,2]
    print(largest_num(list1))