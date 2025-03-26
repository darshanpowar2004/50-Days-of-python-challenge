# Day 43
# Student Marks
student_dict = {}
def student_marks():
    while True:
        student_name = input("Entre Student name or done: ").capitalize()
        if student_name.lower() == "done":
            return student_dict
        student_mark = int(input(f"Enter {student_name} marks: "))

        student_dict[student_name] =  student_dict.get(student_mark, 0) + student_mark
if __name__ == "__main__":
    print(student_marks())