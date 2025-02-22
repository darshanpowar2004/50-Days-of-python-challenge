# Day 19
# Words and Elements

def count_words(a: str):
    txt = a.split(" ")
    return f"{len(txt)} words."

def count_elements(a : str):
    a = a.replace(" ","")
    return f"{len(a)} elements."

if __name__ == '__main__':
    text = "I Love Learning"
    print(count_words(text))
    print(count_elements(text))