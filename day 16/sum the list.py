# Day 16
# Sum The List

def sum_list(arr : list):
    total = 0

    for i in arr:
        total += sum(i)

    return total

if __name__ == '__main__':
    arr = [[2, 4, 5, 6], [2, 3, 5, 6]]

    print(sum_list(arr))