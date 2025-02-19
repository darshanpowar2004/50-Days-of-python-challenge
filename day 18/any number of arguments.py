# Day 18
# Any Number Of Arguments

def any_number(num : list):
    average = sum(num)/ len(num)
    return average

if __name__ == '__main__':
    numbers = list(map(int,input("Enter any number (use ',' for separate) : ").split(",")))
    print(any_number(numbers))
