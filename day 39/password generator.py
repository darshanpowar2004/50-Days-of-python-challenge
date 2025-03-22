# Day 39
# Password Generator
import random as rd
import string

def generate_password():
    while True:
        user = input("How strong password want you pike (weak,strong,very strong): ")
        if user.lower() == "weak":
            user = 5
            break
        elif user.lower() == "strong":
            user = 8
            break
        elif user.lower() == "very strong":
            user = 8
            break
        else:
            print("Invalid Input!")

    password = "".join(rd.sample(string.printable,user))

    return f"Your Password is : {password}"

if __name__ == "__main__":
    print(generate_password())