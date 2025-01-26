def divide_or_square(number):
    if number % 5 == 0:
        square_root = number**0.5
        return f"the number {number} is divisible by 5 than the square root of {number} is {square_root:.2f}."
    else:
        divide = number % 5
        return f"The number {number} is not divisible by 5; therefore, the division of {number} by 5 is {divide}."

if __name__ == "__main__":
    number = int(input("Enter number : "))
    result = divide_or_square(number)
    print(result)