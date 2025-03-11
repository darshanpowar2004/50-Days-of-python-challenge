# Day 35
import string
alphabet = string.ascii_lowercase

def check_pangram(sentence:str):
    wrong_word = True
    for letter in alphabet:
        if letter not in sentence:
            wrong_word = False

    return wrong_word

if __name__ == '__main__':
    sentence = 'the quick brown fox jumps over a lazy dog'
    print(check_pangram(sentence))