# Create User

from data_for_create_user import info

def create_user():
    try:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        password = input("Enter Password: ")
    except Exception as e:
            print("Try Agin",e)
    else:
        info['name'] = name
        info['age'] = age
        info['password'] = password
        print("User saved.Please login")

    with open("data_for_create_user.py", "w") as data:
        data.write(f"info = {info}")

def login():
    while True:
        try:
            name = input("Enter Name: ")
            password = input("Enter Password: ")
        except Exception as e:
            print("Try Agin",e)
        else:
            if info['name'] == name and info['password'] == password:
                print("Logged in successfully")
                break
            else:
                print('Wrong password or user name.Please try again.')

if __name__ == '__main__':
    user = input("login for 0 or create account for 1: ")
    if user == "0":
        login()
    elif user == "1":
        create_user()
    else:
        print("invalid input!")
