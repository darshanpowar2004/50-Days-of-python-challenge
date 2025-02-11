def convert_numbers(arr : list):
    for i in range(len(arr)):
        arr[i] = str(arr[i])
        them = arr[i]

        a = len(them)%3
        lenght = len(them)
        numbers = []
        last_index = lenght
        index = 3
        while index <= (lenght-a):
            numbers.append("," + them[-index:last_index])
            last_index = -index
            index += 3



        numbers.append(them[a-1])

        arr[i] = ''.join(numbers[::-1])


if __name__ == "__main__":
    numbers = [1000000, 2356989, 2354672, 9878098]
    convert_numbers(numbers)
    print(numbers)

# best approach
def convert_numbers(n):
    new_list = []
    for num in n:
        new_list.append("{:,}".format(num)) # learning new thing
    return new_list
print(convert_numbers([1000000, 2356989, 2354672, 9878098]))




