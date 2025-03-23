# Day 40
# Pig Latin

def translate(s : str):
    vowels = ("a","e","i","o","u")
    s_list = s.split()
    pig_latin = []
    for i in s_list:
        if i[0] in vowels:
            pig_latin.append(i+"yay")
        else:
            pig_latin.append(i[1:]+i[0]+"ay")

    return " ".join(pig_latin)

if __name__ == "__main__":
    a = 'i love python'
    print(translate(a))