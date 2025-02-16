# What's My Age

names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}

def your_age (data : dict):
    while True:
        try:
            name = input("Enter your name : ").lower()

            if name not in  data:
                print(f"{name} is not in data.")
                age = int(input("Enter your age : "))
                data[name.lower()] = age

            info = f"Hi,{name.capitalize()},you are {data[name]} years old."

            return  info

        except Exception as e:
            print("Error ! Try agin",e)

if __name__ == '__main__':
    print(your_age(names_age))