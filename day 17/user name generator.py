# Day 17
# User Name Generator

import random as rd

def user_name():
    name = input('Enter Your Name : ')
    num = "".join(map(str,rd.choices(range(0,9),k=rd.randint(1,4))))

    name  = f'{name[::-1]}{num}'

    return name


if __name__ == '__main__':
    print(user_name())