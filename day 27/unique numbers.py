# Day 27
# Unique Numbers

def unique_numbers(arr : list):
    uni_list = []
    for i in arr:
        if arr.count(i) == 1:
            uni_list.append(i)

    sum_evn_odd = sum(arr) - sum(uni_list)

    if sum_evn_odd % 2 == 0 :
        return arr
    else:
        return uni_list

if __name__ == '__main__':
    arr = [1, 2, 4, 5, 6, 7, 8, 8]
    print(unique_numbers(arr))