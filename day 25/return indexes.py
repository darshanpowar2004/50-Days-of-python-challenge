# Day 25
# All the Same

def all_the_same(arr):
    same = True
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            same = False

    return same


if __name__ == '__main__':
    a = ['Mary','Mary','Mary']
    print(all_the_same(a))