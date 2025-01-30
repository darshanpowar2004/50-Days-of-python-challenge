# Register Check

def register_check(registar : dict):
    num_student = 0
    for i in registar.keys():
        if registar[i] == "yes":
            num_student += 1
    return num_student


if __name__ == "__main__":
    register = {'Michael': 'yes', 'John': 'no',
                'Peter': 'yes', 'Mary': 'yes'}

    print(f"The numbers of student in school is {register_check(register)} .")
