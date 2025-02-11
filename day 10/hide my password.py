def hide_password():
    valid_password = True

    while valid_password:
        password = input("Enter your password (minimum 4 characters long): ")

        if len(password) >= 4:
            valid_password = False
        else:
            print("password is less than 4 characters\n")

    password = len(password) * "*"
    return password

if __name__ == "__main__":
    print(hide_password())