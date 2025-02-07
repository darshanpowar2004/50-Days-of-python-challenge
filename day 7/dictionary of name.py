def dictionary_of_name(names:list):
    s_dict = {}

    for letter in range(len(names)):
        if names[letter][0].lower() == "s":
            s_dict[names[letter]] = names.count(names[letter])

    return s_dict

if __name__=="__main__":
    names = ["Joseph", "Nathan", "Sasha", "Kelly","Muhammad", "Jabulani", "Sera","Patel", "Sera"]

    s = dictionary_of_name(names)
    print(s)