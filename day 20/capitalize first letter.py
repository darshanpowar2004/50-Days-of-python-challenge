#Day 20
#Capitalize First Letter

def capitalize(text : str):
    text = text.split(" ")
    new_text = []
    for word in text:
        str1 = word[0].upper()
        txt = str1 + word[1:].lower()
        new_text.append(txt)
    return " ".join(new_text)

if __name__ == '__main__':
    text = "i like learning"
    result = capitalize(text)
    print(result)
