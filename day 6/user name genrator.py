def user_name_gen(mail):
    for i in range(len(mail)):
        world = mail[i]
        if world == "@":
            return mail[:i]


if __name__=="__main__":
    name = input("Enter your mail : ")
    user_name = user_name_gen(name)
    print(f"Your user name is '{user_name}'")