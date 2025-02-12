def swap_value(num : list):
    new_num = num[:]
    them1 = new_num[0]
    new_num[0] = new_num[-1]
    new_num[-1] = them1

    return new_num

if __name__=='__main__':
    numbers = [2,4,67,7]
    print(swap_value(numbers))
    print(numbers)