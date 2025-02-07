def string_range():
    num = int(input("Enter thr number: "))
    string = ""
    for i in range(num):
        string +=  f"{i}"
        if i < num-1:
            string +=  "."

    print(string)

if __name__ == "__main__":
    string_range()