def zeros_last(num_list : list):
    num_list.sort()
    while num_list[0]==0:
        num_list.pop(0)
        num_list.append(0)
    return num_list

if __name__ == "__main__":
    numbers = [2, 1, 4, 7, 6]
    print(zeros_last(numbers))
