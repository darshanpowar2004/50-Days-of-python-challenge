def zeros_last(numbers : list):
    numbers.sort()
    while numbers[0]==0:
        numbers.pop(0)
        numbers.append(0)
    return numbers

if __name__ == "__main__":
    numbers = [2, 1, 4, 7, 6]
    print(zeros_last(numbers))