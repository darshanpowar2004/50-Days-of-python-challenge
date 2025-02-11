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
    num = [1000000, 2356989, 2354672, 9878098]
    convert_numbers(num)
    print(num)





