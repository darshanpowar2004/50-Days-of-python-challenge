def biggest_odd(numbers : str):
    list_odd = [int(x) for x in numbers if int(x) % 2 != 0]

    if not list_odd:
        return "There not any odd number"

    big_odd = max(list_odd)

    return big_odd

if __name__ == "__main__":
    numbers = "23569"
    print(biggest_odd(numbers))