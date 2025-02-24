# Even Number or Average

def even_or_average():
    num = list(map(int,input("Enter any five number (use , for separation): ").split(",")))

    if len(num) != 5:
        return "Plz entre 5 numbers"

    even_num = []

    for  i in num:
        if i % 2 == 0:
            even_num.append(i)

    if even_num:
        return f"the largest even number in the inputted numbers is {max(even_num)}"
    else:
        average = sum(num) / len(num)
        return f"There is no even number in inputted numbers. \nThe average of all five numbers is {average}"

if __name__ == "__main__":
    output = even_or_average()
    print(output)