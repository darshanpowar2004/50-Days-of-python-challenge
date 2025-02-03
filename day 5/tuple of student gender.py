def student_gender(students : list):
    male = 0
    female = 0
    for i in students:
        if i.upper() == "MALE":
            male += 1
        else:
            female += 1

    return [("Male",male),("Female",female)]


if __name__ == '__main__':
    students = ['Male', 'Female', 'female', 'male', 'male', 'male',
                'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

    result = student_gender(students)
    print(result)