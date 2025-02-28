# Multiply Words

def multiply_words(s : str):
    temp_list = s.split(" ")
    mul_word = 1
    for txt in temp_list:
        if txt.islower():
            mul_word *= len(txt)
    return mul_word

if __name__ == '__main__':
    s = "love live and laugh"
    a = "Hate war love Peace"
    result_s = multiply_words(s)
    result_a = multiply_words(a)
    print(s,"=",result_s)
    print(a,"=",result_a)