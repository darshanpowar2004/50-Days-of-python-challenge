# Day 34
# Just Digits

def just_digits(file_name):
    digit_list = []
    with open(file_name,"r") as f:
        csv_file = f.read().split(" ")
        for i in csv_file:
            if i.isdigit():
                digit_list.append(int(i))

    return digit_list

if __name__ == '__main__':
    result = just_digits("python.csv")
    print(result)