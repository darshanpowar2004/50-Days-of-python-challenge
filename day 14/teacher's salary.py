# Extra Challenge : Teacher's Salary

def your_salary():
    teachers_data = {}

    while True:
        teacher = input("Enter Your teacher name (for quit use 'y') : ")
        if teacher.lower() == 'y':
            break
        periods = int(input(f"Enter teacher {teacher} numbers periods (monthly) : "))
        print(" ")


        salary = 0

        if periods > 100:
            salary += 25

        salary += (periods * 20)

        teachers_data[teacher.capitalize()] = [periods,salary]

    for name in teachers_data:
        print("_________________")
        print(f"Teacher : {name}")
        print(f"Periods : {teachers_data[name][0]}")
        gross_salary = teachers_data[name][1]
        print(f"Gross salary : {gross_salary:,}")
        print("_________________")


if __name__ == '__main__':
    your_salary()