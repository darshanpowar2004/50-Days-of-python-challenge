def odd_even(numbers : list):
    odd = [x for x in numbers if x % 2 != 0]
    even = [x for x in numbers if x % 2 == 0]

    if not odd and not even :
        return 0
    elif not odd :
        return max(even)
    elif not even :
        return min(odd)

    return  max(even) - min(odd)

if __name__ == "__main__":
    numbers = [1,2,4,6]

    print(odd_even(numbers))

