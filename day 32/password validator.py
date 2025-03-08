# Day 32
# Password Validator

def password_validator():
    valid_upper = False
    valid_lower = False
    valid_digit = False

    while True:
        password = input("Entre password: ")
        if len(password) < 8:
            print("Password must be 8 characters long.")
            continue

        for i in range(len(password)):
            if password[i].isupper():
                valid_upper = True
            elif password[i].islower():
                valid_lower = True
            elif password[i].isdigit():
                valid_digit = True

        if valid_digit and valid_lower and valid_upper:
            return "Valid Password"
        else:
            print("ERROR!")
            print("password should have at least 'one upper letter','one lower letter','one number'.")
            print("Try another password")


if __name__ == '__main__':
   print(password_validator())